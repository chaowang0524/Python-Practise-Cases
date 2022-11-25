""" Find all Chinese phone number in the text """

import re

content = """
from my reaction — Gatsby, who represented everything for
In my younger and more vulnerable years my father gave
me some advice that I’ve been turning over in my mind ever
since. 18666905244
“Whenever you feel like criticizing any one, ” he told me, “just
remember that all the people in this world haven’t had the advantages that you’ve had.”
He didn’t say any more, but we’ve always been unusually
communicative in a reserved way, and I understood that he
meant a great deal more than that. In consequence, I’m inclined to reserve all judgments, a habit that has opened up
many curious natures to me and also made me the victim of not
a few veteran bores. The abnormal mind is quick to detect and
attach itself to this quality when it appears in a normal person,
and so it came about that in college I was unjustly accused of
being a politician, because I was privy to the secret griefs of
wild, unknown men. Most of the confidences were unsought —
frequently I have feigned sleep, preoccupation, or a hostile levity when I realized by some unmistakable sign that an intimate
revelation was quivering on the horizon
for the intimate revelations of young men, or at least the terms in which they express them, are usually plagiaristic and marred by obvious suppressions. Reserving judgments is a matter of infinite hope. I
am still a little afraid of missing something if I forget that, as
my father snobbishly suggested, and I snobbishly repeat, a
sense of the fundamental decencies is parcelled out unequally
at birth.
And, after boasting this way of my tolerance, I come to the
admission that it has a limit. Conduct may be founded on the
hard rock or the wet marshes, but after a certain point I don’t
care what it’s founded on. When I came back from the East last
autumn I felt that I wanted the world to be in uniform and at a
sort of moral attention forever
I wanted no more riotous 13609188112
464547812367
excursions with privileged glimpses into the human heart. Only
Gatsby, the man who gives his name to this book, was exempt
which I have an unaffected scorn. If personality is an unbroken
series of successful gestures, then there was something gorgeous about him, some heightened sensitivity to the promises
of life, as if he were related to one of those intricate machines
that register earthquakes ten thousand miles away. This responsiveness had nothing to do with that flabby impressionability which is dignified under the name of the “creative temperament.”— it was an extraordinary gift for hope, a romantic
readiness such as I have never found in any other person and
which it is not likely I shall ever find again. No — Gatsby
turned out all right at the end
it is what preyed on Gatsby,
what foul dust floated in the wake of his dreams that temporarily closed out my interest in the abortive sorrows and shortwinded elations of men.
My family have been prominent, well-to-do people in this
Middle Western city for three generations. The Carraways are
something of a clan, and we have a tradition that we’re descended from the Dukes of Buccleuch, but the actual founder of my
line was my grandfather’s brother, who came here in fifty-one,
sent a substitute to the Civil War, and started the wholesale
hardware business that my father carries on to-day.
I never saw this great-uncle, but I’m supposed to look like
him — with special reference to the rather hard-boiled painting
that hangs in father’s office I graduated from New Haven in
1915, just a quarter of a century after my father, and a little
later I participated in that delayed Teutonic migration known
as the Great War. I enjoyed the counter-raid so thoroughly that
I came back restless. Instead of being the warm centre of the
world, the Middle West now seemed like the ragged edge of 18967899654
the universe — so I decided to go East and learn the bond business. Everybody I knew was in the bond business, so I supposed it could support one more single man. All my aunts and
uncles talked it over as if they were choosing a prep school for
me, and finally said, “Why — ye — es, ” with very grave, hesitant faces. Father agreed to finance me for a year, and after
various delays I came East, permanently, I thought, in the 18827966457
spring of twenty-two."""


# Chineses phone number format:
# start from 1, second digit from 3 to 9, total 11 digits
def find_phone_number(content: str) -> list:

    result = re.findall(r'[1][3-9]\d{9}', content)
    return result


print(find_phone_number(content))
