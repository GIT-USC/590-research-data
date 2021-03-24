SecReq

SecReq-Team: Siv Hilde Houmb, Shareeful Islam, Jan Jürjens, Eric Knauss*, Kurt Schneider 	 

(* corresponding author (knauss@chalmers.se))

The goal of SecReq [2] is to assist all steps in security requirements elicitation, as well as providing mechanisms to trace security requirements from high-level security statements (security objectives) to rather secure design. The approach aims at bridging the gap between security best practises and the lack of security experience among developers and designers. SecReq combines three distinctive techniques that have been integrated to meet this goal: (1) Common Criteria [1] and its underlying security requirements elicitation and refinement process, (2) the HeRA tool [4] with its security-related heuristic rules, and (3) the UMLsec tool set [3] for security analysis and design.
Eliciting Security Requirements and Tracing them to Design: An Integration of Common Criteria, Heuristics, and UMLsec

Building secure systems is difficult for many reasons. Our work [2] deals with two of the main challenges: (i) the lack of security expertise in development teams, and (ii) the inadequacy of existing methodologies to support developers who are not security experts. The security standard ISO 14508 (Common Criteria) together with secure design techniques such as UMLsec can provide the security expertise, knowledge, and guidelines that are needed. However, security expertise and guidelines are not stated explicitly in the Common Criteria. They are rather phrased in security domain terminology and difficult to understand for developers. This means that some general security and secure design expertise are required to fully take advantage of the Common Criteria and UMLsec. In addition, there is the problem of tracing security requirements and objectives into solution design,which is needed for proof of requirements fulfilment. In [2], we describe a security requirements engineering methodology called SecReq. SecReq combines three techniques: the Common Criteria, the heuristic requirements editorHeRA, andUMLsec. SecReqmakes systematic use of the security engineering knowledge contained in the Common Criteria and UMLsec, as well as security-related heuristics in the HeRA tool. The integrated SecReq method supports early detection of security-related issues (HeRA), their systematic refinement guided by the Common Criteria, and the ability to trace security requirements into UML design models. A feedback loop helps reusing experiencewithin SecReq and turns the approach into an iterative process for the secure system life-cycle, also in the presence of system evolution.

Read more at Springer Requirements Engineering Journal.
Supporting Requirements Engineers in Recognising Security Issues

More and more software projects today are security-related in one way or the other. Security often becomes a problem if an environment was initially not considered security-related, but security issues are discovered later. In such a situation, there may not be any security experts available to assist in requirements activities. Therefore, requirements engineers often fail to recognise early indicators for security problems. Ignoring security issues early in a project is a major source of the recurrent security problems we are experiencing in practise today. The first round of requirements identification and analysis is labour-intensive and error-prone. There is a high risk to neglect security in order to finish on time and in budget.

We address this problem by presenting a toolsupported method that provides assistance for requirement engineering, with an emphasis on security requirements. The HeRA tool applies heuristics to requirement statements in order to identify security-relevant issues. This tool was now extended by a trained Bayesian classifier. Requirements that are classified as potentially security-relevant are handled with specific care. This early classification helps to focus and save time and money. HeRA is integrated in a workflow of requirements analysis and reuse of experiences, thus increasing security awareness within the software development process. We validate the approach at the hand of several industrial requirements documents and the results are promising.
Resources

In order to let others reproduce our results, we will share our data and tools here.

    Expert Classification of requirements: In order to train and evaluate heuristic classifiers that identify security-relevant requirements, we need pre-classified requirements. Download our Expert-Classification of ePurse-Specification.
    Training and Testdata: From the expert classification, we derive sets of classified requirements for training and evaluation. These are simple CSV files, for the three specifications in our evaluation: ePurse, CPN, and GPS.
    Evaluation tool: In order to apply our training and evaluation datasets, we created a tool that manages the evaluation. It allows to load different datasets, apply them to a heuristic classifier, and evaluate the results. Please download and try our Evaluation Tool.
        Extract the Zip, start the secreqEvaluationTool.jar, and add one or more of the specifications from above via the file menu.
        Specify, which requirements should be used for training either manually or via the edit menu.
        Train and use the classifier via the Actions menu. Resize the window, to make the statistics in the bottom line visible.
        Use Tools - explain selected to analyse the data. If a requirement is selected, the tool displays the information it has about each word in the requirement. If no requirement is selected, the tool shows the trained database.
        To get a visualisation of the performance of the classifiers, use Actions - K-fold cross validation. The analysis uses the requirements already loaded, but ignores training and classifier selections. We used a Bayesian classifier with classic parameters for our evaluation.

References

    ISO 15408:2007 Common Criteria for Information Technology Security Evaluation, Version 3.1, Revision 2, CCMB-2007-09-001, CCMB-2007-09-002 and CCMB-2007-09-003, September 2007.
    Siv Hilde Houmb, Shareeful Islam, Eric Knauss, Jan Jürjens, and Kurt Schneider. Eliciting Security Requirements and Tracing them to Design: An Integration of Common Criteria, Heuristics, and UMLsec. Requir. Eng., 15(1):63-93, March 2010.
    Jan Jürjens. Secure Systems Development with UML. Springer Academic Publishers, Heidelberg, 2005.
    Eric Knauss, Daniel Lübke, and Sebastian Meyer. Feedback-Driven Requirements Engineering: The Heuristic Requirements Assistant. In 31st International Conference on Software Engineering (ICSE 2009), pages 587-590, Vancouver, Canada, 2009.
    Knauss, E.; Houmb, S.; Schneider, K.; Islam, S. & Jürjens. Supporting Requirements Engineers in Recognising Security Issues. In Proceedings of 17th Intl. Working Conference on Requirements Engineering: Foundation for Software Quality (REFSQ'11), Springer, 2011


