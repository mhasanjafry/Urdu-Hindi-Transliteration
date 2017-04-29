# Urdu-Hindi-Transliteration
“One man’s Hindi is another man’s Urdu” (Rai, 2000). We aim to transcribe written hindi sentences into written urdu sentences and vice versa using the two language's phonetic equivalence

Urdu, the national language of Pakistan, has been influenced by Arabic and Persian, while Hindi, national language of India contains words from “Sanskrit”. 
Both languages are very different in terms of writing styles as the former is written in “Nastaleeq” script while the latter is written in Devanagari script.
Urdu is written from right to left while Hindi is written from left to right. Interestingly, the two languages sound very similar, in the words of (Rai 2000), 
“One man’s Hindi is another man’s Urdu”.. So, while native speakers of both languages can talk to each other, they can’t understand each other’s written scripts.
Therefore we want to do textual translation between the two languages based on the concept of phonetic similarity idea.

This idea may seem simple in theory but poses many practical challenges.
First of all, a single Hindi character may map to a combination of two characters. This happens for many characters  eg: Ghar is written as shown in hindi and 
urdu respectively. With “Gh” split into G + h.

Same phenomenon occurs at word level too. There are some words in Urdu which are represented by a single word in Hindi. The problem is worsened by the fact that
those words can appear in separate form too.

Perhaps the worst problem of all is the absence of diacritical marks which are not written in Urdu, even though they are critical for correct pronunciation and disambiguation of
certain words. E.g. a single character ب  can produce the sound ba, bi or bu depending on what the missing diacritical mark is. Similarly, we observed that corresponding to many Urdu
characters there are multiple mappings into Devnagri script (example و -> व, ो , ो , ो , ो ,
ऊ, ओ, औ). Grammar rules and context are needed to select the appropriate Devnagri
character for such Urdu characters.

Previous research done on this problem can be broadly divided into 2 areas: Rule based approach [1],[2] and Statistical methods (SMT) [3],[4]. To begin with we integrated different
rule based approaches proposed by various papers. After which, some enhancements made by us included:
  1. Coming up with some of our own rules to increase the accuracy of our system. 
  2. Choosing the most likely sequence of words based on our character level language model. The model was developed in two ways:
        - Treated each character individually
        - Clustered alphabets together based on the observation that combinations of Urdu characters map to a single character in Hindi before training our SMTs.


