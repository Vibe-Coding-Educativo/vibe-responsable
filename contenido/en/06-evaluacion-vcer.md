# The VCER evaluation

## What the VCER evaluation is

VCER stands for «vibe coding educativo responsable», the Spanish for responsible educational vibe coding. It is the evaluation proposed by the guide «Responsible vibe coding» to check whether an educational resource meets the essentials of the guide before it is published or used. It is suitable for any finished resource, one's own or someone else's, whether or not it was created following the guide.

The evaluation is carried out by an AI using a [file of instructions](#how-to-evaluate-a-resource) that is downloaded from the guide. The AI reviews the code of the resource, scores each point of the rubric with 2, 1 or 0, justifies each score and proposes the three improvements that would raise the result the most.

## How the result is calculated

The percentage is the sum of the scores divided by the maximum possible for the points the AI has been able to check. Content and personal data are disqualifying. From the percentage and those two points, one of these three results is obtained:

| Result | When it applies | What it means |
| --- | --- | --- |
| **Recommended** | 70 % or more, with content and personal data scored and with no 0 in either of them or in accessibility | The resource meets the essentials of the guide and can be used or published. The proposed improvements complete it. |
| **Needs improvement** | Less than 70 %, or when the content or the personal data could not be checked, or accessibility has a 0 | The resource has flaws that should be fixed before publishing or recommending it, although none of them rules it out. The report says what they are and what remains to be checked. |
| **Not recommended** | A 0 in content or in personal data, whatever the percentage | The resource has obvious errors in what it teaches or sends students' data to services outside the school. It should not be used with students or published until it is fixed. |

## Limits of the evaluation

The AI only detects the errors it sees, especially in the content, and the result may vary depending on the model used. That is why the score is indicative and does not replace a review by a person. In addition, the result applies to the version of the resource that was evaluated, on the date of the evaluation.

## How to evaluate a resource

The evaluation file, which appears below, is given to the AI together with the resource to be evaluated, and the AI is asked to «evaluate this resource according to the instructions». How to give it depends on where the resource is:

- **If it was created on a chatbot's website or on an app-building platform**, the file is attached, or its text pasted, in the same conversation, once the material is finished.
- **If it is in a folder on the computer or in a repository**, the file is given to a coding agent or a code editor with AI opened in that folder. This is the most complete way, because the AI can read all the files of the project and, if it can run code, test the resource in the browser.
- **If only the published website is available**, one's own or someone else's, a conversation with the AI is opened and the evaluation file and the code of the page, saved from the browser, are attached. If the website is made up of several files, the AI will only see the ones it is given, so it is advisable to obtain the complete code, for example from its repository, and evaluate it as in the previous case.

<!-- evaluacion -->

The AI scores each recommendation with the VCER rubric, gives a final percentage and proposes the three improvements that would raise the score the most. If it is then asked to fix it, it first proposes the changes and waits for them to be approved; it is advisable to save a copy beforehand. If the resource is one's own, the AI also offers to save the report in the project and to add to the footer of the material a mention with the result, linked to this page.

## The VCER rubric

Each point of the rubric checks one of the recommendations of the guide, which is developed in its chapter. This is the rubric used by the evaluation file:

<!-- rubrica -->
