# Before publishing: ten recommendations

## 1\. Review the content without delegating the review to the AI

Artificial intelligence (AI) can make mistakes with complete naturalness, and an error in a simulation or a quiz ends up as mistaken learning. Before publishing, the material has to be used as students would use it, checking the concepts, the data and the answers it accepts as correct. This review cannot be delegated, since responsibility for what is taught lies with the person who publishes it.

- **Minimum.** Go through the material from beginning to end, also with wrong answers, and use subject expertise to check every result. After each significant change, repeat the walkthrough with a checklist that the AI itself can draft, since a small modification can break something that already worked.
- **Recommended.** Ask the AI to turn that checklist into automated tests and run them after every change.

## 2\. Do not send personal data to services outside the school

Students' names, marks, voices or images are personal data. In Spain, the Spanish Data Protection Agency states in its [guide for schools](https://www.aepd.es/documento/guia-centros-educativos.pdf) that teachers must use the tools provided by the school or the education authority, and that content a teacher publishes on their own, outside the school, is their own responsibility. Other countries have different rules, but the precaution is the same. The simplest way to comply is for the material not to ask for data. When a tool needs to identify students, such as a gradebook, the data must stay on the teacher's device or in the systems the school has decided to use. Particular care is needed with platforms that easily add user accounts and databases, since the data are then stored on third-party servers.

- **Minimum.** Do not ask for real names or anything that identifies a person, unless the tool needs it to do its job, and in that case store it only on the device. Ask the AI whether the application sends information to any server. If the material opens inside a platform, check whether it requires registration or a minimum age before sending the link to students, since they are being taken to a third party's service.
- **Recommended.** Publish the material on a site that students can open without registering, and check that the code contains no web addresses of unrecognised services. When the program is going to manage students' data in the school's systems, the decision belongs to the school, and a technical review is advisable before putting it into use.

## 3\. Understand what the material does

If nobody understands how a resource works, it cannot be fixed when it fails, and in practice it stops being open. Meeting this point does not require knowing how to program, since it is enough to be able to describe briefly what the application does, what it stores and whether it communicates with any external service.

- **Minimum.** Ask the AI to explain in plain language what the application does and whether it stores or sends anything, and check that the explanation matches what can be observed when using it. Also ask for the material's own code to be commented and readable, since code compressed into endless lines is reason enough not to publish. Well-known libraries that are included are the exception, as they are usually distributed that way.
- **Recommended.** Add a document explaining how the project is organised and what each file is for.

## 4\. Do not depend on services that may disappear

A resource that embeds content from another website, or loads parts from third-party servers, stops working when those services change or close. The same happens with the platform where the material was created, since the shared link lasts as long as the company decides.

- **Minimum.** Keep a copy of the material's code on the teacher's own computer, and update it when it changes.
- **Recommended.** Ask the AI to load whatever the material needs from outside from well-known services and to record it in the decision log, and keep the project's own images, texts and data inside it.

## 5\. Make it accessible to everyone

Materials generated with AI tend towards the showy, and decorative effects are often an obstacle for some students. An accessible resource can be used without a mouse, can be understood without relying on colour and reads well on a small screen.

- **Minimum.** Ask the AI from the start to follow the accessibility guidelines, and test the result with the keyboard only, with enlarged text and on a phone.
- **Recommended.** Ask the AI to check accessibility with an automated tool and fix what it detects. Coding agents can do this unaided, since they install the tool, run it and apply the fixes.

## 6\. Credit the creators of material taken from others

The images, texts, sounds and pieces of software that are incorporated have authors and licences, even if the AI placed them there. The attribution must go inside the material itself, so that it travels with it when it circulates out of context.

- **Minimum.** State the author, source and licence of each third-party element, and replace those that do not allow reuse.
- **Recommended.** Also check the licences of the software libraries included, since some of them determine the licence of the whole.

## 7\. Keep a record of how it was made

With AI, work moves very fast, and a few weeks later nobody remembers why each decision was taken. Keeping that record makes it possible to resume the work, to explain it to someone else and not to undo by mistake something that had a reason.

- **Minimum.** Keep a document with the important decisions and their reasons. The AI itself writes it when asked at the end of each working session, and all that remains is to review and save it.
- **Recommended.** Ask the AI to keep a decision log or ADR (*Architecture Decision Record*) inside the project. The AI writes it from what is decided in the conversation, with the context, the discarded alternatives and the consequences of each decision and, for technical ones, what it is based on and how it was checked. All that remains is to check that what is recorded matches what was decided.

## 8\. Declare the use of AI and what has been checked

In a resource created with vibe coding, the code is the work of the AI, and usually nobody has reviewed it line by line. The people who reuse it need to know this in order to decide how far they can trust it. It is therefore advisable to state which tool was used to create it and, above all, what the person who publishes it has checked, such as the correctness of the content, how it works or how data are handled.

- **Minimum.** One or two sentences inside the material, next to the licence, with the tool used and what has been checked.
- **Recommended.** The same statement in the project documentation, with a link to the decision log from point 7, which is what explains how the material was made.

## 9\. Publish with a visible free licence

Works are protected by copyright automatically, so a resource without a licence cannot be safely reused even if it has been published. A free licence tells other people that they may use it, adapt it and share it, and on what conditions. Code and content need different licences, and what the AI generates raises questions of authorship that are dealt with in its chapter.

- **Minimum.** Write the author and the licence inside the material itself, in a visible place, for example in the footer.
- **Recommended.** Add the licence file to the project, with a free software licence for the code, such as AGPL v3 or MIT, and a free Creative Commons (CC) licence, such as CC BY-SA or CC BY, for the content.

## 10\. Offer the code so that others can adapt it

The licence gives permission, but the material must also be obtainable in a form that allows work to be done on it. That way someone else can adapt it to their classroom without asking anyone for anything.

- **Minimum.** Offer the code for copying or downloading, together with the decision log from point 7, so that someone else can continue it.
- **Recommended.** Publish it in an open repository, with an explanation of how to use it and how to modify it, and ask the AI to mark each published version with a version tag, which makes it possible to retrieve the exact code of that version later.
