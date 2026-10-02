# Offer the code so that others can adapt it

## Openness in practice

A free licence gives permission to reuse a resource, but **the permission falls short if the material cannot be obtained in a form that allows work to be done on it**. The [Recommendation on Open Educational Resources (OER)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer) of the United Nations Educational, Scientific and Cultural Organization (UNESCO) does not speak only of access, but of re-use, re-purposing, adaptation and redistribution. Free software puts it in a similar way with its [four freedoms](https://www.gnu.org/philosophy/free-sw.en.html), which include the freedom to study how the program works and change it, and the freedom to distribute copies of modified versions, for which access to the code is a necessary condition. The [Declaration on libre knowledge](https://wikieducator.org/Declaration_on_libre_knowledge) extends the same idea to any knowledge resource: it is free when anyone can use it for any purpose, learn from it, copy it, adapt it and share the result for the benefit of the community.

The article [«Mantener la "A" de abierto en los REA en tiempos de IA»](https://cedec.intef.es/mantener-la-a-de-abierto-en-los-rea-en-tiempos-de-ia/) (Keeping the "O" of open in OER in times of AI), from the National Centre for Curriculum Development in Non-Proprietary Systems (CEDEC), makes this concrete in a principle of adaptable simplicity, according to which it is better to prefer what is functional and simple to what is complex and closed, and the quality criterion of a resource is that it can be reused.

## Obtaining the material

The minimum is for the material to offer its code for copying or downloading. On a chatbot's website and on app-building platforms the code can usually be viewed, but other people only receive a link, so it is advisable to add to the material itself the way of obtaining it, or to publish it separately. Together with the code, it is advisable to offer the decision log of recommendation 7, which allows someone else to continue it without having to guess why it is made that way.

The recommended step is to publish the project in an open repository, with an explanation of how to use it and how to modify it. A repository also allows other people to propose improvements and the author to incorporate them.

In a repository the code keeps changing after it is published, so the link to the project always leads to the most recent version. To retrieve later the exact version that was published, used in class or evaluated, **it is advisable to mark each published version with a version tag**, or *tag* in Git terminology, such as v1.0 or v1.1. The AI creates it when publishing, and it is enough to tell it once in its instructions. A tag that has already been published is not moved or reused, because it would stop pointing to what was published. Next to it, the identifier of the *commit* can be recorded, the code that Git assigns to each saved state of the project, which serves as an exact reference even if the tag were changed by mistake.

## A resource that is easy to adapt

**A resource is more reusable when the content is separated from the functionality**. A quiz whose questions are in a list at the beginning of the code, or in a separate file, can be adapted to another subject by changing that list, without touching the rest. It is advisable to ask the artificial intelligence (AI) for this from the start, together with the commented code of recommendation 3 and the absence of dependencies of recommendation 4, which are the other two conditions that make adaptation easier.

It also helps to state in the documentation which parts are meant to be changed, such as the texts, the colours or the language. Someone who wants to translate the material, or adjust it to another educational level, thus finds where to start.
