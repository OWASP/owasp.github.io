---

date: 2024-03-01 00:00:00-0700
categories: blog
author: Luca Pascal Rotsch
author_image: /assets/images/people/leader_luca_rotsch.jpg
layout: blogpost
title: Introducing the OWASP IoT Security Testing Guide (ISTG)
excerpt_separator: <!--more-->

---

The multitude of networked devices contributing the Internet of Things (IoT) poses new risks for manufacturers, operators, and end users of solutions. Every IoT device represents potential threats to user data and supporting infrastructure when a single manipulated device has potential to endanger an ecosystem. Due to the interconnection of an array of technologies, standards and protocols, a considerable amount of effort is necessary to build and maintain a homogeneous level of IoT security.

To reduce the risk of successful attacks, manufacturers and operators must periodically assess the security level of their IoT solutions. An instrument for this purpose is penetration testing such as goal based security assessments tailored toward target systems. We are excited to announce that the [OWASP IoT Security Testing Guide](https://owasp.org/www-project-iot-security-testing-guide/) project published its first release on March 1, 2024. This guide aims to provide comprehensive insights into testing the security of IoT devices and systems.

<!--more-->

([read more about our motivation, challenges and goals](https://github.com/OWASP/owasp-istg/blob/main/src/01_introduction/README.md#motivation))



## Who is this guide for?

The OWASP IoT Security Testing Guide is intended for penetration testers and security analysts in the IoT, hardware, and embedded fields. Penetration testers and bug bounty researchers can use the concepts introduced in the [IoT Security Testing Framework](https://github.com/OWASP/owasp-istg/blob/main/src/02_framework/README.md) to plan their tests, define the test scope, test conditions and test approach. While performing the test, the test cases in the [Test Case Catalog](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/README.md) and the respective [Checklists](https://github.com/OWASP/owasp-istg/blob/main/checklists) can be used:

- as a guide that shows which aspects should be tested, why they should be tested, how they should be tested and how potential issues could be mitigated as well as
- to keep track of the test completion status, making sure that all relevant aspects have been examined.



However, others might benefit from the concepts and test cases introduced in this guide as well:

* **Manufacturers of IoT devices** (e.g., architects, engineers, developers and managers) can use the contents of this guide to get an understanding of potential issues and vulnerabilities that might affect their products. By increasing the awareness and understanding early on in the design and development process, it is possible to improve product security in the long term while keeping the respective costs as low as possible.

- **Security consultants and security managers** can use this guide and its contents as a common foundation for working with their teams and clients as well as communicating with any of the stakeholders mentioned above. Especially the terminology and structure defined in this guide should help to facilitate collaboration across different teams and organizations.


- **Operators of IoT devices** (e.g., users) can use this guide in a similar fashion as manufacturers. However, the operators who run IoT devices usually have no or very little influence on the design and development process. Hence, their focus is more directed towards understanding how a device might be vulnerable in a particular operational environment and how this environment could be affected in case that the device is compromised or insecure.

([read more about the intended audience](https://github.com/OWASP/owasp-istg/blob/main/src/01_introduction/README.md#intended-audience))



## How does it work?

The following (simplistic) examples shall demonstrate how the ISTG can be used to plan and execute penetration tests of different IoT devices. Feel free to have a look at the full documentation of the [IoT Security Testing Framework](https://github.com/OWASP/owasp-istg/tree/main/src/02_framework) and the [Test Case Catalog](https://github.com/OWASP/owasp-istg/tree/main/src/03_test_cases).



### Scenario 1: CCTV Camera

CCTV cameras are commonly used to monitor and surveil public places as well as private properties. The operators of such cameras rely on their flawless functionality for various reasons, incl. safety and security. Any failure may result in serious consequences, which is why manufacturers and operators of such cameras should, ideally, have a high interest in securing their products.

For various reasons (e.g., budget, time, responsibilities, development and testing model etc.), it does not always make sense to perform full-fledged, all-encompassing tests of complete devices. Sometimes it is better to focus on individual parts and interfaces based on a certain threat model. The ISTG provides tools, namely the [device model](https://github.com/OWASP/owasp-istg/blob/main/src/02_framework/device_model.md) and [attacker model](https://github.com/OWASP/owasp-istg/blob/main/src/02_framework/attacker_model.md), that can be used to describe different kinds of IoT devices and threats (attackers) in a straightforward fashion.



So, let's assume that the manufacturer of a CCTV camera brand wants to conduct a penetration test of their product. Before starting with the penetration test, manufacturer and penetration tester analyze typical characteristics of CCTV cameras:

* Wall-mounted = out of reach / usually not (easily) physically accessible
* (Potentially) installed in a public place = many people have access to the area, the camera is installed in
* Connected to a video management system = has a wired or wireless network connection



Based on these characteristics, a potential attacker could be described as follows:

* They could try to attack the camera locally via the local network or a wireless interface of the camera. The attacker model describes this as *physical access level 2 (PA-2) "local access"*.
* They could be anyone visiting the area that the camera is installed in. They are not associated with either the manufacturer or operator of the camera nor do they need to have any registered account etc. This is called *authorization access level 1 (AA-1) "unauthenticated access"* in the attacker model.



Since components and test cases within the ISTG are associated with the access levels described in the attacker model, it is now easily possible to narrow down the applicable test scope given the defined threat scenario:

* [x] Test of [wireless interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/wireless_interfaces/README.md) (e.g., Wi-Fi)
* [x] Test of [data exchange services](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/data_exchange_services/README.md), running on the device (e.g., video streaming service)
* [x] Test of [user interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/user_interfaces/README.md) (e.g., a web dashboard)
* [ ] Test of the [processing unit](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/processing_units/README.md)
* [ ] Test of the [device memory](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/memory/README.md)
* [ ] Test of the [installed firmware](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/firmware/installed_firmware.md) and [firmware update mechanism](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/firmware/firmware_update_mechanism.md)
* [ ] Test of [internal interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/internal_interfaces/README.md)
* [ ] Test of [physical interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/physical_interfaces/README.md)



### Scenario 2: Smart Home Device

Smart home devices are part of many modern households. From the smart lightbulb over the smart fridge to the smart garage opener, they are part of many aspects of our lives. As more and more people rely on smart devices, they have become attractive targets for attackers. Many of those devices process private data of some sort or are even responsible for controlling access to private property.



Analog to scenario 1, let's assume that the manufacturer of a smart home device wants to have their product tested. The device may have the following characteristics:

* Can be bought by anyone (incl. attackers)
* Installed in private homes
* Convenience first, (unfortunately) security second = different kinds of users with varying expertise must be able to install and use the device; hence, they are designed focusing on the ease of use, usually providing some kind of user interface



Using the aforementioned [attacker model](https://github.com/OWASP/owasp-istg/blob/main/src/02_framework/attacker_model.md), potential attackers can be described as follows:

* They can analyze their own device and might be able to prepare and reproduce attacks against devices of their victims. Since they have their own device at home, they have full physical access to the device. They could even disassemble it any analyze the device internals if necessary. The attacker model describes this as *physical access level 4 (PA-4) "invasive access"*.
* They have access to some kind of user interface, allowing them to monitor, control or even configure the device. This is called *authorization access level 2 (AA-2) "low-privileged access"* or *authorization access level 3 (AA-3) "high-privileged access"* respectively in the attacker model.



With these access levels, it may be possible to attack all device components. Hence, the applicable test scope in this threat scenario would include:

* [x] Test of the [processing unit](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/processing_units/README.md)
* [x] Test of the [device memory](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/memory/README.md)
* [x] Test of the [installed firmware](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/firmware/installed_firmware.md) and [firmware update mechanism](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/firmware/firmware_update_mechanism.md)
* [x] Test of [data exchange services](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/data_exchange_services/README.md)
* [x] Test of [internal interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/internal_interfaces/README.md)
* [x] Test of [physical interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/physical_interfaces/README.md)
* [x] Test of [wireless interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/wireless_interfaces/README.md)
* [x] Test of [user interfaces](https://github.com/OWASP/owasp-istg/blob/main/src/03_test_cases/user_interfaces/README.md)



## What's next?

This guide is not a monolithic, all-encompassing instruction manual for IoT device penetration testing. Instead, it should be seen as a dynamic and growing collection of test cases for various technologies related to IoT devices.

In its current state, this guide comprises test cases on a very high and generic level. This is intentional since the base version of this guide should be applicable to as many different IoT devices as possible (*comparability*). However, the long-term goal is that this guide will be expanded over time by adding modules with more detailed test cases for specific technologies (*expandability*). Thereby, the guide will evolve and become more and more detailed over time.



### Join us and help us shape the future of IoT security testing!

By contributing to this project, you'll have the opportunity to shape and enhance the understanding of IoT security testing practices.

To contribute, please head over to our [GitHub repository](https://github.com/OWASP/owasp-istg). Here you can review the project's documentation, code and share your valuable feedback following the projects [contribution guidelines](https://owasp.org/www-project-iot-security-testing-guide#div-contributing). Your expertise and insights will play a crucial role in improving the guide's quality and relevance. Whether you are an experienced IoT security tester or someone passionate about ensuring the security of connected devices, your contributions are highly welcome. Join us in this collaborative effort to strenghten IoT security testing practices and make a positive impat on the industry! Thank you for your support and dedication to IoT security. Together, we can make a difference.
