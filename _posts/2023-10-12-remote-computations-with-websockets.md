---
date: 2023-10-12
categories: blog
author: Franklin Pezzuti Dyer
author_image: /assets/images/people/Franklin_Pezzuti_Dyer.jpg
layout: blogpost
title: Doing remote computations with WebSockets
---

The following write-up is from a blog post originally published on the [author's personal website](https://franklin.dyer.me/post/199).

#### The common phenomenon of remote code execution

What I'd like to describe in this entry isn't by any means a new idea or a very complex one, but rather a very simple idea that's very easy to forget as we surf the web. When you visit a web page, your browser, which is a multi-process application on your computer, opens a connection with a remote server, through which it downloads the page's HTML code. If there are some necessary resources not included in the HTML, for instance images, CSS styles or JavaScript code, additional messages can be sent to the server to request these resources and incorporate them into the representation of the page that the browser presents to you. The HTTP and HTTPS protocols describe how this process works.

Of course, the mere act of downloading code from an untrusted remote source presents some amount of danger - if I, the owner of the remote server, could execute whatever code I wanted on your computer, then I'd be able to steal all of the sensitive data on your device, install software that lets me spy on your activities or take advantage of your processor remotely, etc. But if your interactions with the internet take place through the interface of your browser, and that browser doesn't have any security holes, then it will make sure not to allow remote code to touch your computer's filesystem without your explicit permission. In the past there certainly have been cases of unsafe browsers that made possible data theft or filesystem manipulation by remote entities, and this would be considered a vulnerability of those browsers.

But in order for most webpages to function correctly, the JavaScript code that your browser downloads has to be executed, and any kind of code execution involves using your computer's CPU. Therefore, as soon as you access a webpage on a good and secure browser, your local filesystem will remain inaccessible to the remote entity with which you're establishing a connection, but you're certainly inviting it to make use of your CPU. Sure, you're not inviting it to make *exclusive* use of your CPU - your computer's operating system will determine how the various processes being executed on your computer share the CPU, including the processes spawned by your browser. Like any other process, it will have to wait its turn, but with the timeslice of your CPU that your operating system assigns it, it can do what it pleases when it comes to computations, without this usage being considered a security violation.

<center>![Fig 1](https://github.com/franklindyer/blog-image-hosting/blob/main/2023-03-13-Fig1.png)</center> 

Some web applications involve continuous communication between the local process that executes on the client and the server process that runs remotely. This is also generally considered to be legitimate. Imagine, for example, that you access a videogame in the browser, which involves downloading various multimedia resources (audio, images, etc) that should probably occur dynamically for performance reasons (it would be best not to download the resources involved in the videogame all at once, but rather just those that will be needed in the near future).

So, if I'm offering a webpage from a server of mine, I can probably count on a pretty considerable chunk of CPU from whatever person accesses it, in addition to the ability to communicate constantly with the process of my design that's being executed on their computer. After all, this is exactly what most webpages do, so they don't have much right to complain if I decide to take advantage of the slice of CPU that they've allocated for me. And if I choose to do, say, cryptocoin mining or some other task for my own benefit in addition to whatever is strictly necessary for the webpage to work correctly, how will this user ever know the difference, without sitting down to decipher the obfuscated JavaScript that I've sent them? (In fact, pretty soon, we will see one possible way that a user might notice that something like this is happening.)

Coming up, I'll show how a simple web server can take advantage of the CPU slices allocated for managing its web page on client computers that access it, in order to solve computational problems. I wouldn't say that what I'm showing here is practical or efficient - I intend it only as a simple demonstration of what I've just described, and as a reminder of what you're allowing a remote server to do on your computer when you access one of its web pages in a way that's considered secure.

#### Remote integer factorization

Now let's see how we can take advantage of other peoples' CPUs to factor large integers. Okay, I don't personally have any reason to be factoring integers - I just want to show off a simple example of an application that manages to get its hands on the results of computations without actually carrying out any computations on its own, other than whatever is involved in sending and receiving messages over the internet.

We'll use a Python package called Flask to offer a webpage that carries out prime factorizations in the background. First, we'll create a HTML file with the following body:

<div class="code"><code><pre>
Here is something super entertaining that holds a lay person's attention...
</pre></code></div>

In the page's head, we can include some JavaScript code, for instance the following function that factors prime numbers:

<div class="code"><code><pre>
function pfactors(n) {
   var factors = [];
   var d = 2;
   while (n > 1) {
      while (n % d == 0) {
         factors.push(d);
         n = n / d;
      }
      d++;
   }
   return factors;
}
</pre></code></div>

Sure, it's not the most efficient algorithm, but it suffices for illustrative purposes. On the remote server, we'll stick an HTML file with these contents in the directory <code>static/html</code>, which is where our Python server will look for it when it receives a request. Now let's write the server. With the following simple code we can serve the HTML page that we just wrote:

<div class="code"><code><pre>
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
</pre></code></div>

At this point, we're not doing anything other than sending the webpage to the client. If I start up the remote Python server and then visit the address <code>XX.XXX.XX.XXX:5000</code> in my browser (where <code>XX.XXX.XX.XXX</code> is the IP address of my server, which I'm choosing not to divulge) the page that we've just written appears. And although at this point it isn't carrying out any remote computation, we can verify that the <code>pfactors</code> function that we wrote is at least *available* in the client's browser. If I open my browser console, I can carry out a factorization manually:

<div class="code"><code><pre>
> pfactors(100)
< [2, 2, 5, 5] 
</pre></code></div>

To do computations remotely on the client, I'll implement the following very simple protocol:

- When the webpage loads, the client establishes a connection with the server using a WebSocket.
- The server sends the client a random integer to be factored.
- Upon receiving an integer over the connection, the client factors it using <code>pfactors</code> and returns the result to the server via the same connection.
- Upon receiving an answer from the client, the server sends it another random integer to be factored.
- The server and client continue like this until the connection is closed (by the client).

We can modify the server's code like this:

<div class="code"><code><pre>
from flask import Flask
from flask_sock import Sock
import random

def write_factors(n, res):
    with open("factors.txt", "a") as datafile:
        datafile.write(str(n) + " -> " + res + "\n")

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@sock.route('/factoring')
def factoring(ws):
    while True:
        n = random.randint(2, 10**10)
        ws.send(str(n))
        text = ws.receive()
        write_factors(n, text)
        print("A number has been factored.")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
</pre></code></div>

and add the following JavaScript code to the HTML page that we're serving:

<div class="code"><code><pre>
var ws = new WebSocket("ws://XX.XXX.XX.XXX:5000/factoring")

ws.onmessage = function(evt) {
   var received = evt.data;
   ws.send(pfactors(Number(received)));
}
</pre></code></div>

Then, if I start up the server again, open the webpage in my browser for a few seconds as if I were reading it, and then close the window, we find that a few factorizations have appeared in the <code>factors.txt</code> file on the server:

<div class="code"><code><pre>
7328499434 -> 2,17,257,838693
3792814921 -> 7,41,13215383
4083310343 -> 7,37,15765677
4401689293 -> 643,757,9043
3979661166 -> 2,3,3,3,13,89,63697
6915352069 -> 6277,1101697
393300005 -> 5,7,11237143
5359459099 -> 19391,276389
2532264950 -> 2,5,5,50645299
3794691709 -> 1237,3067657
7519596251 -> 31,242567621
9625185328 -> 2,2,2,2,11,37,1478069
645966521 -> 41,167,94343
</pre></code></div>

It's worth noting as well that the process launched by this webpage was among the most expensive processes on my computer. For instance, by using the <code>top</code> command to compare the CPU usage of the active processes on my computer, I notice that the value of the <code>%CPU</code> statistic of the process corresponding to this webpage hovers around <code>99%</code>. It's worth mentioning that a value of <code>99%</code> for the <code>%CPU</code> statistic *does not mean* that my computer's CPU spends $99\%$ of its time executing this process and a mere $1\%$ executing all the rest of its processes, but rather that this process is using $99\%$ of the CPU time that the kernel assigns it. If we interpret this statistic the wrong way, this seems much more grave than it actually is. Most likely, this process isn't receiving more dedicated CPU time than any of the other processes launched by my browser - but of the time that it receives, it actually uses a much higher percentage of that time, since it has a lot of computations to carry out. In fact, it could be that it's receiving *less* dedicated CPU time than other processes, since some scheduling algorithms penalize processes that use up a larger proportion of their CPU time.

#### Practical considerations

Now I'd like to suggest a question: is it actual feasible to take advantage of expensive computations carried out in a hidden and distributed way through the browsers of the visitors to a certain webpage? It's not too hard to show that this is *possible* - we just did so. But what I'm unsure of is whether this can be implemented in a way that is actually advantageous, for various reasons:

- Even though the remote server can save CPU this way, it has to communicate constantly over the network, which also presents costs.
- A process launched to execute a webpage's JavaScript code probably won't receive a huge slice of CPU.
- If the browser detects that a particular window's code is using a lot of CPU, it might alert the user to the possibility that this webpage is malicious.
- The user could close the window and end the process at any time.

So, even if I was the owner of a website with millions of visitors (I wish!) I probably still wouldn't be able to count on a single connection lasting more than, say, a few minutes at most (although would depend on how entertaining my content is, haha). Not only that, but if the connection closes before the computation is finished, all of the progress made up to that point will be lost. For instance, if we modify the previous example so that the server chooses random integers from the interval $[2,10^{15}]$ instead of $[2,10^{10}]$, we can observe that it often happens that the script doesn't manage to factor any integers at all, or perhaps just one or two, over the course of a few minutes. So if this technique were being used to solve some computational problem, it would have to be a *massively parallelizable* problem that can be decomposed into tiny pieces, each of which can be solved in a few minutes at most.

I can think of one way of adapting our code to account for the possibility that the connection could be lost at any moment, and with it all of the work that has been completed but not yet communicated. It could be possible to periodically inform the server of the state of the computation even before it finishes. For instance, the function <code>pfactors</code> can take a long time to return a value if we use it to factor very large integers, but all of the information necessary to reconstruct the computation's process in any moment is present in the values of the three variables <code>n, d, factors</code>. If the client process ends before it finishes the factorization, but it has already told the server that it had reached a value of <code>d = 500000</code> with a still-empty array of factors, then there would be no need for the next process to pick up the job on a different client to start from scratch with <code>d = 500000</code>, since it's already known that there are no factors less than <code>500000</code>. As a challenge, I've decided to try modifying the previous code so that the clients send the server a status update every time <code>d</code> reaches a multiple of <code>10000000</code>. Here's the modified server code:

<div class="code"><code><pre>
from flask import Flask
from flask_sock import Sock
import random

jobs = [[random.randint(2, 10**10)]*2 + [2] for i in range(100)]

def write_factors(n, res):
    with open("factors.txt", "a") as datafile:
        datafile.write(str(n) + " -> " + res + "\n")

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@sock.route('/factoring')
def factoring(ws):
    global jobs
    active = True;
    print("Connection established.")
    while active:
        job = jobs.pop()
        ws.send(str(job)[1:-1])
        print(str(job)[1:-1])
        while (job[1] != 1) and active:
            try:
                text = ws.receive()
                print("Progress update: " + text)
                job = [int(x) for x in text.split(",")]
            except:
                jobs = jobs + [job]
                print("The job was abandoned in state " + str(job))
                active = False
        if active:
            write_factors(job[0], str(job[3:]))
            print("A number has been factored.")

if __name__ == '__main__':
    app.run(host="0.0.0.0")
</pre></code></div>

The desired factorization jobs are generated first in a list, which will be used as a global variable shared by the threads that the server launches for the different WebSockets. A partially completed task is represented by a list where the first three elements represent the number that is meant to be factored, the original number divided by the factors already found, and the value of <code>d</code>, and the rest of the elements represent the factors that have already been found. Hence, a task that hasn't even been started yet is saved as the list <code>[n,n,2]</code>. When the server receives an update from the client, it detects whether or not the task has been finished so that it can assign the client another task in this case, and if it finds that that the connection has been closed unexpectedly, the progress received up to that point is saved by inserting the most recent progress update into the global list of jobs again. Here's the modified client code:

<div class="code"><code><pre>
function pfactors2(state, ws) {
   var n = state[0];
   var m = state[1];
   var d = state[2];
   var factors = state.slice(3);
   while (m > 1) {
      while (m % d == 0) {
         factors.push(d);
         m = m / d;
      }
      if (d % 10000000 == 0) {
         ws.send([n,m,d,factors]);
      }
      d++;
  }
  ws.send([n,m,d,factors]);
}

var ws = new WebSocket("ws://XX.XXX.XX.XXX:5000/factoring")
      
ws.onmessage = function(evt) {
   var received = evt.data;
   var state = received.split(",").map(Number);                                                              
   pfactors2(state, ws);
};
</pre></code></div>

In this new version of the function called <code>pfactors2</code>, a reference to the WebSocket is passed as an argument so that updates can be sent continuously. If I start up the server again and access the webpage on my laptop, but close the window before the computation finishes, I can see that the next time I open the webpage, the unfinished factorization of the same integers is resumed without losing *all* of the progress obtained previously.

I still have doubts that this model could ever be advantageous, but at the very least it seems interesting. There's a lot of research out there that investigates the parallelization of various computational problems, but another puzzle entirely would be the design of algorithms that can function in parallel *and recover from the frequent loss of processors*. I'll close this post with an interesting and relevant theoretical problem:

> Suppose that you're executing jobs as we've described on the computers of people who visit your website, and that the time it takes for a user to close the window can be described as a random variable that follows the exponential distribution $\text{Exp}(\tau^{-1})$ with average time $\tau$. The partial progress of a computation can be saved by sending it to the server, but the client has to spend $\delta$ seconds of its allotted computational time each time that it prepares and sends an update. If any work that hasn't been saved at the time when the user closes the window is considered lost, and the "amount of work" done by the client grows linearly at a certain rate $\sigma$ in each instant that it's not preparing an update, how often should updates be sent in order to finish the greatest amount of computation possible at the clients' expense?
