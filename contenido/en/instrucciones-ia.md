# Instructions for creating an open educational resource

These instructions come from the guide «Responsible vibe coding», for
publishing educational materials created with vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/en/).
Follow them throughout the work, together with what I ask you about the
material I want to create. The material will be published openly, so that
other people can use and adapt it.

## Before starting

If I have not told you, ask me:
- The authorship that should appear (a name or a username).
- Where it will be published: a chatbot's website, an app-building platform,
  or a repository or one's own site.

## How it must be built

- Licence: CC BY-SA 4.0 for the content and AGPL v3 for the code, unless I
  indicate others.
- If we are working on a chatbot's website, make the material as an HTML
  page that works on its own when opened in the browser, and not as a
  component that only works inside the chatbot.
- You may use libraries, typefaces and other external resources when they
  save work or improve the result. Load them from a well-known, stable
  service, and record them in the decision log, with their licence. If any
  part of the material would stop working when the downloaded copy is
  opened on a computer without an internet connection, tell me in simple
  words, for example: «if you open it without internet, the formulas will
  not display».
- Personal data: do not ask for the name or any data that identifies a
  person, unless the tool needs it to do its job, such as a gradebook. In
  that case store it only on the device and offer the option to export or
  print without the names. If the program collects students' answers, show
  the result at the end or let it be downloaded for handing in, and identify
  each person with a code instead of their name. Do not send anything to any
  server or add analytics or visit counters.
- Accessible, following the Web Content Accessibility Guidelines (WCAG):
  usable with the keyboard only, with a logical tab order, labels on the
  controls, alternative text on images, sufficient contrast, not relying on
  colour to understand anything and readable on a mobile phone screen.
- Readable code, commented in the language of the material, not
  compressed, with understandable variable names.
- In the footer of the material: the title, the authorship, the licence with
  its link and a short statement on the use of AI, with the tool, the month
  and year, and what I have checked (ask me before publishing).
- If you incorporate images, sounds or code fragments by other people, use
  only material whose licence allows reuse, and state its authorship, source
  and licence within the material itself.
- If the program is going to store students' data in the school's systems,
  do not write keys or passwords in the code that reaches the browser, make
  sure only the teacher or the school can read what is collected, and tell
  me what a person with technical knowledge should review before it is put
  into use.
- After each change, check again what already worked: run the tests if there
  are any or, if you cannot, tell me which checks I should repeat.

## If it is published in a repository or on one's own site

- Add a LICENSE file with the licence of the code and another with that of
  the content, and state the licence at the top of each code file with an
  SPDX-License-Identifier line.
- Add a document explaining how the project is organised and what each file
  is for.
- Keep a decision log (ADR) inside the project, with one file per decision
  recording the context, the discarded alternatives and the consequences.
  Record in it every decision we take, without waiting for me to ask. For
  technical decisions, also record what you base them on (official
  documentation, a specific version of the code or a test that can be
  repeated), the known risks and how you checked it. Do not invent sources
  or tests: mark whatever you have not been able to check as a hypothesis
  pending validation.
- Check accessibility with an automated tool and fix what it detects.
- When we publish a version, mark it with a version tag (v1.0, v1.1…) and do
  not move or reuse a tag once it has been published.

## When you finish the material

- Briefly describe what the material does, what it stores and whether it
  communicates with any external service.
- Prepare a short checklist with the main walkthroughs and the edge cases,
  to repeat after each change. If the project allows it, turn it into
  automated tests.
- Write a short note with the important decisions you have taken and the
  reason for each one, or summarise them from the decision log if there is
  one.
- Tell me what I should check myself, starting with the correctness of the
  content.
