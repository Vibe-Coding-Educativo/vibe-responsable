# Instructions for evaluating an open educational resource (VCER evaluation)

These instructions come from the guide «Responsible vibe coding», for
publishing educational materials created with vibe coding
(https://vibe-coding-educativo.github.io/vibe-responsable/en/).
They are for evaluating an existing resource, one's own or someone else's,
whether or not it was created following the guide.

## How to evaluate

- Work on the code of the resource I give you. If you do not have it, ask me
  for it before starting.
- Do not fix it: only evaluate it.
- Score each of the ten points with 2, 1 or 0 according to the VCER rubric
  (responsible educational vibe coding, from its Spanish initials), and
  justify each score with a sentence about what you have seen in the
  resource.
- If a point cannot be checked with what I have given you, leave it
  unscored and say what would be needed to check it.
- Before scoring, make a complete inventory, not a sample: every function
  that asks for or stores data about people and how it is exported or
  copied; every image, sound, video, icon and typeface in the project, and
  where it comes from (look at the images: a redrawn logo is still someone
  else's); and everything that is loaded from outside, and when (on opening,
  when something is pressed or in a new window).
- If the resource is published, evaluate that version or check that it
  matches the code you have been given. Record which version you have
  evaluated: the version tag and the commit if it is in a repository, or the
  address and the date of the evaluation if it is not.
- For point 5, if you can run code, open the resource in a browser and run
  an automated accessibility tool on it, such as axe-core, also with content
  loaded and not only on the initial screen. Do not count what is embedded
  from other sites. The tool does not check keyboard use: go through it with
  the Tab key. In the justification of the point, say what you have tested
  and how; if you have only been able to read the code, say so.

## VCER rubric

1. CONTENT (disqualifying)
   2: No errors are detected in what it teaches: the data, the definitions
      and the answers it accepts as correct.
   1: There is some minor inaccuracy in what it teaches.
   0: There are obvious errors in concepts, data or answers.
   This score only reflects the errors you have detected: list each one and
   point out what a person should check. Typos and formatting errors in the
   references do not count here: point them out separately.

2. PERSONAL DATA (disqualifying)
   2: It does not ask for data that identifies anyone, or it stores them
      only on the device and allows exporting without names; or it sends
      them only to a school service, with no keys visible in the code and in
      such a way that only the teacher or the school can read them. It has
      no analytics.
   1: It does not send students' data to outside services, but it stores
      names without an option to export without them, or the sending to the
      school's service is not well protected (keys in the code, an address
      that allows what is collected to be read).
   0: It sends students' data to a server outside the school, or it has
      analytics or tracking.
   If the resource handles real students' data, state that a review by a
   person with technical knowledge is advisable before using it.
   What is loaded or embedded from other servers (videos, audio, typefaces,
   libraries) is assessed in point 4, not here.

3. UNDERSTANDING WHAT IT DOES
   2: What it does, what it stores and what it communicates with can be
      described briefly, and the resource's statements match its code.
   1: Its operation can be understood, but there are parts whose purpose is
      unclear or it does not explain what it stores.
   0: There are functions or communications whose purpose cannot be
      explained, or what it declares does not match the code.

4. DEPENDENCIES
   2: What it loads or embeds from outside comes from well-known services
      and is recorded, and its own texts, images and data are inside the
      material.
   1: It loads or embeds external resources without recording them, or part
      of its own content (a video, an audio recording, a map) is only on another
      platform.
   0: The main content depends on an external service, or it loads code from
      unknown addresses.

5. ACCESSIBILITY
   2: It can be used entirely with the keyboard, the controls have labels,
      the images alternative text, the contrast is sufficient, it does not
      rely on colour and it adapts to a narrow screen.
   1: It fails in one or two of those aspects, without preventing its use.
   0: It fails in three or more, or it cannot be used with the keyboard.

6. THIRD-PARTY MATERIAL
   2: Each third-party element states its author, source and licence, and
      the licence allows it to be reused; or there is no third-party
      material.
   1: There is third-party material with a valid licence, but not fully
      credited.
   0: There is third-party material without a licence that allows reuse or
      without any attribution.

7. RECORD
   2: There is a log or a note with the important decisions and their
      reasons.
   1: There is documentation explaining how it is made, but not why.
   0: There is nothing.

8. USE OF AI
   2: It states that it was made with AI and what the person has checked.
   1: It states that it was made with AI, without saying what has been
      checked.
   0: It does not state it. If it is stated that no AI was used, it is not
      scored.

9. LICENCE
   2: Authorship and a free licence visible in the material, with a link. If
      it is a multi-file project, it includes the licence file.
   1: The authorship or the licence is missing, the licence is not free (NC
      or ND) or it does not link to its text.
   0: It states neither authorship nor licence.

10. REUSE
   2: The code can be obtained in full, it is understandable when read, with
      comments where needed, and there are instructions for modifying it.
   1: It can be obtained, but it is hard to understand without comments, it
      is partly compressed or it has no instructions for modification.
   0: It cannot be obtained, or it is obfuscated or compressed.

## Result

- Calculate the percentage: the sum of the scores divided by the maximum
  possible for the points scored.
- Give a result: «Not recommended» if point 1 or 2 has a 0, whatever the
  percentage; «Needs improvement» below 70 %; «Recommended» from 70 %, as
  long as points 1 and 2 could be scored and point 5 does not have a 0. If
  either of points 1 and 2 has been left unscored, the result is «Needs
  improvement» and states what remains to be checked; if point 5 has a 0, it
  is also «Needs improvement» and states what prevents its use.
- Start the report with a line such as «VCER rubric: Recommended (85 %)»,
  followed by another with the version evaluated, and add below it a
  sentence with what that result means:
  - Recommended: it meets the essentials of the guide and can be used or
    published; the proposed improvements complete it.
  - Needs improvement: it has flaws that should be fixed before publishing
    or recommending it, although none of them rules it out.
  - Not recommended: it has obvious errors in what it teaches or sends
    students' data to services outside the school; it should not be used or
    published until it is fixed.
- In the justification of point 3, include that brief description. In that
  of point 4, list the external addresses in the code and what each one is
  for, and say in simple words what would stop working when opening the
  downloaded copy on a computer without an internet connection. In that of
  point 6, list the third-party material.
- End with the three improvements that would raise the score the most.

## If I then ask you to fix it

- Before changing anything, tell me what you would change and wait for me
  to approve it. Do not change the content or how it works, unless I ask
  you to.
- If there is no decision log, write one that describes how the resource
  works now, and state that it was written afterwards.
- If the licence or the statement on the use of AI is missing, prepare the
  text for me to add it.
