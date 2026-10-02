# Do not depend on services that may disappear

## A material's dependencies

A material depends on an external service when it needs something that is not inside it in order to work. The most common forms are content embedded from another website, programming libraries and typefaces loaded from third-party servers, and connections with online services. The platform where the material was created is also a dependency, when the material only exists within it.

These dependencies are not visible when using the material. They are discovered by reading the code or by asking the artificial intelligence (AI) to list them, which is what point 4 of the [VCER evaluation](para-la-ia.html#to-evaluate-an-existing-resource) asks for.

## Changes in external services

An external service may change its terms, become paid or close, and the material that depended on it **stops working without its author having touched anything**. The article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/) (Keeping the "O" of open in OER in times of AI), which the National Centre for Curriculum Development in Non-Proprietary Systems (CEDEC) devotes to open educational resources (OER), illustrates this with the case of a resource that embeds an interactive map from an external platform. If the platform withdraws free presentations, the resource shows a blank box, and the teacher cannot recover the content because they do not have the original file. The article recommends reserving embedded content for videos and similar cases.

The risk is not only that the service disappears. In 2024, the polyfill.io domain, from which more than one hundred thousand websites loaded a widely used library, changed hands and began serving malicious code without the affected pages having changed anything, as documented by the security company [Sansec](https://sansec.io/research/polyfill-supply-chain-attack). The same CEDEC article warns of another risk specific to AI-generated code: invented libraries, or libraries impersonated by others with an almost identical name.

## A platform's link

When the material has been created on a chatbot's website or on an app-building platform, the shared link lasts as long as the company decides. A change in the service, in its terms or in the teacher's account can render that link useless, and with it all the pages that have embedded it.

**The minimum is to keep a copy of the material's code on one's own computer** and update it when it changes. With that copy the material can be recovered, published elsewhere or further developed with another tool. For it to be useful, the material has to be a page that opens on its own in the browser. The most widely used chatbots, such as ChatGPT, Gemini or Claude, often generate the application as a React component, a very widespread programming library, which only works within their own website. That is why the [instructions file for the AI](para-la-ia.html) asks them for an HTML page.

## What is loaded from outside

Programming from scratch what a well-known library already solves is not realistic, and neither is hosting inside the material everything it uses. Libraries that display formulas, charts or maps, and typefaces, can be loaded from outside, provided they come from a well-known service and are recorded. A well-known service does not guarantee that it will stay the same either, and that is why it is advisable to check what stops working when the material is opened offline.

The recommended step is to ask the AI to load these resources from well-known services and to record them in the decision log of recommendation 7, with their licence. That list is not meant for the teacher, but for fixing or adapting the material later on, a task that will often be done by an AI again. What cannot be retrieved from elsewhere, such as one's own images, texts and data, should be inside the material, or at least kept in a copy, and not only embedded from another platform.

What matters most to the teacher is a practical consequence: **whether the material will keep working when opened, downloaded, on a computer without internet**, for example in a classroom without a connection. The check requires no technical knowledge, since it consists of opening the material, disconnecting the device from the network and loading it again. One example is [Tantrix](https://felipsarroca.github.io/jocs/Tantrix/), a game by Felip Sarroca that can be installed as an application and works offline after the first visit. The VCER evaluation asks the AI to explain it in simple words, of the kind «if you open it without internet, the formulas will not display».
