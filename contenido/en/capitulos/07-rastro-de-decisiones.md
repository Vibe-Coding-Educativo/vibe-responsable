# Keep a record of how it was made

## The reason for each decision

With artificial intelligence (AI), programming moves very fast, and **a few weeks later nobody remembers why each decision was taken**. Ernesto Serrano, from the eXeLearning team, describes it in his talk [«Inteligencia artificial: programar, documentar y no acabar en un berenjenal»](https://erseco.github.io/talks/charlas/2026-07-06-selia-ia-programar-documentar/unit/index.html) (Artificial intelligence: programming, documenting and not ending up in a mess): the code is there, but the why is not, and nobody remembers which alternatives were discarded or on what grounds. AI does not cause that disorder, although it makes it arrive sooner.

Keeping the record serves three purposes. It makes it possible to resume the work after some time without having to reconstruct it, to explain it to someone else who wants to continue it, and to avoid undoing in good faith a decision that had a reason. In an open educational resource it has a fourth use, since it shows the people who reuse it how it was made, which is what completes the statement of recommendation 8.

## The decision log

The usual way to keep it in software development is the architecture decision record, or ADR (*Architecture Decision Record*). Each important decision is recorded in a short document that includes four things:

- **The context.** The situation that makes a decision necessary.
- **The decision.** What is done, in enough detail to apply it.
- **The discarded alternatives.** Each one with the reason it was not chosen, which is the part that avoids repeating the debate later on.
- **The consequences.** What improves and what gets worse.

A decision that stops being valid is not deleted, but marked as superseded by the new one, so that the record is preserved. In the project presented in the talk, each record also notes with which AI tool and which model the decision was taken, which makes it possible to change tools without losing the history.

In that same project, each record also includes the evidence on which the decision is based, the known risks and the way it was validated. The talk sums it up in the rule «no source, no claim»: every fact refers to the official documentation, to a specific version of the code or to a test that anyone can repeat. This precaution is especially useful with AI, since it can write a convincing justification for a decision that starts from a false premise. The recorded evidence lets the person check it without redoing the work. Whatever could not be verified is recorded as a hypothesis pending validation, so that nobody later takes it for a checked fact.

## The work of the AI and the work of the person

**The log is not an additional task for the teacher**, since the AI writes it from what is decided in the conversation, and the person checks that what is recorded matches what was decided. The talk sums it up by saying that the AI makes proposals and the person makes the decisions.

Nor is the log reconstructed at the end, since a resource usually comes out of many working sessions spread over different days, and putting those conversations back together afterwards is unfeasible. **The log is written at the moment the decision is taken**, and that is why it is preserved from one session to the next. Coding agents are told once in their instructions file, and they keep it up in all sessions. It is advisable to ask for it by name, for example «keep a decision log with ADRs», since the AI knows the format and applies it without further explanation. On a chatbot's website, the minimum is to ask the AI at the end of each session to record that day's decisions in a document that is kept and added to.

## An example from the community

The interactive guide [«Elige tu IA»](https://explikarlos.github.io/elige-ia/) (Choose your AI), published as expliCarlos, has a [decision log](https://github.com/explikarlos/elige-ia/blob/main/docs/decisions/ADR-001-static-pages.md) in its repository. The first record explains why the application is static and has no server. Among the discarded alternatives is a database, which would have allowed answers to be synchronised, but which was discarded because it increased privacy risks, cost and maintenance. Anyone who takes up that project knows that the absence of a server is the result of a considered decision.

This guide also has its own [log](https://github.com/Vibe-Coding-Educativo/vibe-responsable/tree/main/docs/adr), which records the decisions about its sources, its website and its examples.
