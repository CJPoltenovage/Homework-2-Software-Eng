


<!-- AI use 

1: What I delegated:

I gave the AI the code information and used it to find all sections oif redundant code I needed to replace as well as recommendations for tests that I can use to ensure functionality is presereved through my refacting process. I also used it to explain to me what the errors in my code were that would cause my tests to fail and what I may need to change to realign my code changes with the test suite. -->


<!-- 2: One suggestion you accepted and how you verified it:

A suggestion I accepted and verified was the use of helper fiunctions in is_starving, is_snacking_hungry, and is_exhausted. I verified them using a set of tests in test_models.py that called them directly in order to verify correct values were being given. 





3: one suggestion, assumption, or output you rejected or changed — and why.:

One suggestion I changed was the AI's plan to put all of the care rules in a new
care_policy.py file. I decided to keep them at the top of models.py instead to
keep the change small and easy to follow. The reason I chose to ignore it was because my way would still solve the main problem, and because every rule is only defined once, it avoided adding an extra file that the app didn't really need yet.


-->



