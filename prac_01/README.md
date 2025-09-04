# Practical 01
IntermediateExercises
 Okay, let’spractiseusingPyCharmtowritesimpleprograms.
 1. SalesBonus
 File: sales_bonus.py
 CreateanewPythonfileintheprac_01directorycalledsales_bonus.py,andcopythefollowingdocstring
 atthetopofthefile.Adocstringisatriple-quotedspecialcomment“doc(umentation)string”.
 """
 Programtocalculateanddisplayauser'sbonusbasedonsales.
 Ifsalesareunder$1,000,theusergetsa10%bonus.
 Ifsalesare$1,000orover,thebonusis15%.
 """
 NowwritethePythoncodetocompletetheprogramaccordingtothatdocstring.
 Thefirst linemight looklike:
 sales=float(input("Entersales:$"))
 Runandtestthecodewithafewdifferentvaluestoverifythat itworks.
 Wheneveryouaretestingcode,youshouldnotjustuserandomvaluesbutvaluesthatyouknowtheexpected
 outputforandthattestallpathsofexecution, includingtheboundaryoredgecase.
 So, forthisprogramwecouldusethefollowing(we’reonlyinterestedinthevalues,nottheformat):
 TestInput ExpectedOutput
 500 50
 2000 300
 1000(edgecase) 150
 Now(onlywhentheabovepart isfinished),addalooptothis,soitrepeatedlyasksfortheuser’ssalesand
 printsthebonusuntiltheyenteranegativenumber. (Notetheboundarycarefully.)
 Rememberthatuntil istheoppositeofwhile,andifyouneedhelp,pleasecheckthepatterns.Here’s(only)
 someofthepseudocodetohelpyou:
 getsales
 whilesales>=0
 calculatebonus
 getsales
 donextthing(ifneeded)
 2.Debugging:
 File: broken_score.py
 Someone(it’snotpolitetosaywho)wastryingtowriteaprogramtotelltheuseriftheirscoreisinvalid,
 bad,passableorexcellent,buttheircodeisinthe“bad”categoryanddoesn’twork.
 Rewritethefollowingprogrammingattemptusingthemostefficientif-elif-else‘ladder’youcan.Thecodeis
 availablehereat: broken_score.py
 RemembertoclickRawbeforecopyingandpastingsoyougetproperformatting!
 Theintentionisthatthescoremustbebetween0and100inclusive;90ormoreisexcellent;50ormoreisa
 pass;below50isbad.
 Beverycarefulofyourboundaryconditions... andtest!
 6
3. Loops
 File: loops.py
 Create a file called loops.py and add this for loop that displays all the odd numbers between
 1 and 20 with a space between each one.
 for i in range(1, 21, 2):
 print(i, end=' ')
 print()
 Now write more for loops (using range) to do the following:
 (Note that for marking, we expect to see a complete file with each loop still in it.)
 a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
 b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
 c. print n stars. Ask the user for a number, then print that many stars (), all on one line
 Note: this is a very simple loop for repeating n times. We use for loops for “definite” iteration like this.
 while loops are used for “indefinite” iteration (like repeating while a user input is incorrect).*
 Sample output:
 Number of stars: 4 ****
 d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting
 at 1. E.g. if 4 was the number entered, your single loop should print
 • ***
 Keep going...
 We’ve now had the walkthrough and the intermediate exercises where you mostly have existing code to
 modify and extend, or you have to write something really similar to working code you’ve been given...
 Nowwemoveontothesection where you are given a task/goal to complete with no starting code. Remember to
 use the examples done above as a guide, and if you’re not sure how to do it, go back to the subject materials. For
 example, the question below asks for an error-checking loop, which we cover in chapter 2 (Control), and which is
 also summarised as one of our standard patterns at: https://github.com/CP1404/Starter/wiki/Programming
Patterns
 If you need help, ask a classmate or your tutor.
 