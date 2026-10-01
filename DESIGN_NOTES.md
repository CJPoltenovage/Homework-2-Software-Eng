

<!-- # "Rquested changes in my own words 
The project needs me to implement a "Care Board" which must show one and only one recommendation for dragong care depending upon howhungry and how much energy puff has The recommendation should also prioritize what action is taken, for example if puff is very tired but only a little hungry he should still be recommendewd to be fed before resting. Additionally the care board recommendation should match the other places where recommendationsa re made so that conflicting instructions are not given. Addtionally I must create and add tests that demonstrate each Care Board recommendation, at least one priority case in which multiple conditions are true, preservation of important existing behavior, and the behavior of any refactored code I depend on
--> 


<!-- Current behavior that must be preserved
I think that all of the feeding functionality must be preserved exactly as it is. When Puff is fed at hunger 8 or higher his hunger drops by 3, his energy goes up by 1, and he becomes "relieved." When his hunger is between 5 and 7 it drops by 2 and he becomes "happy," and when it is below 5 it drops by 1 and he becomes "sleepy." His hunger should also never go below 0 and his energy never above 10. Most of the status message code should stay the same too, so it should still say "very hungry" at hunger 8 or higher, "could use a snack" at hunger 6 or 7, "exhausted" at energy 2 or lower, and otherwise show his mood or "doing fine." needs_attention() should still return True when hunger is 8 or higher, energy is 2 or lower, or his mood is "sleepy." The home page should still show the URGENT banner when he is very hungry, and feeding him from the page should still update him and redirect. The only part of status message that really needs to change is when his hunger is 6 or 7 and his energy is 2 or lower, where it should say he is exhausted instead of needing a snack so it matches the Care Board telling him to rest. Additionally, all existing tests should not change or fail.

<!-- Design Problems 
One design problem is that the feeding and rest check rules are written in a bunch of different places instead of just one. The check for hunger 8 or higher shows up in feed(), status_message(), and needs_attention() in models.py, and again in the home() method in views.py. The snack and rest checks are also repeated in both status_message() and home(). This is a problem because if the daycare ever changes one of these numbers, every version of the rule checks has to be found and changed, and if one gets missed then we won’t satisfy our consistency requirement. Another design problem is that nothing in the code controls which care rule should win when more than one applies. Both the banners in home() and status_message() just go with whatever order their if statements happen to be written in, and both look at hunger before energy so currently our prioritization is incorrect. 



<!-- Proposed Structural Changea
My plan is to define all of the care rules once at the top of models.py, outside of the Dragon class. This will cover when Puff is very hungry, needs a snack, or is exhausted, along with small functions that check those values to make sure updates to the mood and recommendation are made as needed. Then feed(), status_message(), needs_attention(), and the banner in home() will all use these instead of their own numbers, so the view will stop making its own care decisions. During the refactor I will keep every check in its current order so the app behaves exactly the same. I will add one function that returns the Care Board recommendation in the right priority order as well, and have the banner and status_message() use it so they always match the Care Board. That way, any future change to a number or to the priority only has to be made in one place. -->



<!-- Part 5 -->


<!-- What did you change structurally?:
What I changed structurally is that  I moved the hunger and energy numbers into named constants at the top of models.py and added three functions, is_starving, is_snacking_hungry, and is_exhausted, to check them. Then I updated feed(), status_message(), needs_attention(), and the banner in views.py to use these instead of their own numbers. For the feature I added care_recommendation(), which returns the first rule that matches in priority order, and now the banner and status_message()
both use it, so the view no longer makes its own care decisions.



What did you change behaviorally?:

The home page now shows a Care Board with one recommendation: FEED NOW, REST,
OFFER SNACK, or ALL CLEAR. The only old behavior that changed is when Puff's
hunger is 6 or 7 and his energy is 2 or lower. Before, the banner and status
message said he needed a snack, but now they say he needs rest so they match the
Care Board. Everything else, including feeding, works the same as before.




What evidence gives you confidence that existing behavior was preserved?:

The evidencse that gives me confidence that existing behavior was preserved is
that all of the baseline tests, along with my added characterization tests,
passed after the refactor without me changing them. The only test I changed was
the hungry and exhausted one, which I updated on purpose becuase the stakeholder
wanted REST to win over OFFER SNACK. I also added tests for the new functions
and the Care Board, and all of those tests passed ensuring that the behavior that those tests depended on also functioned as intended.




How would the NEXT similar change be easier because of your design?:

If the daycare wanted to change a value, such as increasing the snacking threshold by one, it only has to be chnaged in one place now instead of four. This makes it far easier to add code or change functionalities without breaking any existing behavior or causing code contradictions.




What is one design tradeoff or limitation you chose not to address?:

One limitation I chose not to address is that the needs_attention function
doesn't use the Care Board recommendation. It still relies on the same shared
functions, so its numbers will always match, but if the
priority rules are changed in the future, someone would need to remember to check
needs_attention to make sure it still works as intended.