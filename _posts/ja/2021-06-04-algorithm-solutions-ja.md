---
audio: false
generated: false
image: false
lang: ja
layout: post
title: アルゴリズムの問題の解決方法
translated: true
---

このファイルは、GitHubプロジェクト[https://github.com/lzwjava/algorithm-solutions](https://github.com/lzwjava/algorithm-solutions)のREADME.mdです。

---

# アルゴリズム問題の解決策

オンラインジャッジプラットフォームからのいくつかのアルゴリズム問題の解決策です。

| プラットフォーム | 問題が解決された |
| ------------- | ------------- |
|[UVa](https://uhunt.onlinejudge.org/id/113519)|568|
|[Codeforces](https://codeforces.com/profile/lzwjava)|419|
|[LeetCode](https://leetcode.com/lzwjava/)|20|
|[Hacker Rank](https://www.hackerrank.com/profile/lzwjava)|20(SQL)|

|言語|行数|
|----|----|
|Java|70851|
|C++|3214|
|Python|1193|
|SQL|101|

このリポジトリには、Codeforces、HackerRank、LeetCode、Lintcode、Nowcoder、UVaのプラットフォームからのさまざまなアルゴリズム問題の解決策が含まれています。 各解決策は問題番号ごとに整理されており、ソースコード、入力ファイル、そして場合によっては追加のドキュメントが含まれています。

## リポジトリの構造

- `README.md`: このファイルです。
- `codeforces/`: Codeforcesの問題の解決策を含む。
- `hacker_rank/`: HackerRankのSQL問題の解決策を含む。
- `leetcode/`: LeetCodeの問題の解決策を含む。
- `lintcode/`: Lintcodeの問題の解決策を含む。
- `nowcoder/`: Nowcoderの問題の解決策を含む。
- `uva/`: UVaの問題の解決策を含む。

### Codeforces

`codeforces`ディレクトリ内の各サブディレクトリは、問題番号で名前付けされており、次のものを含んでいます。

- `1.in`: 問題の入力ファイルです。
- `src/Main.java`: 問題の解決策を含むJavaソースコードファイルです。

### HackerRank

`hacker_rank`ディレクトリには、さまざまな問題のSQLファイルが含まれており、各ファイルは解決する問題の名前が付いています。

### LeetCode

`leetcode`ディレクトリには、異なる問題用のPythonスクリプトが含まれており、ファイル名は解決する問題の名前です（例：`two_sum.py`または`valid_parentheses.py`）。

### Lintcode

`lintcode`ディレクトリ内の各サブディレクトリは、問題番号で名前付けされており、次のものを含んでいます。

- `src/com/lintcode/Main.java`: ソリューションのメインクラスファイル
- `src/com/lintcode/Solution.java`: 問題のソリューションクラスファイル
- `src/com/lintcode/`: 問題によって必要な追加のクラスファイル。

### Nowcoder

`nowcoder`ディレクトリ内の各サブディレクトリは、問題の名前で名前付けされており、次のものを含んでいます。

- `Solution.java`: 問題のソリューションクラスファイル
- `Test.java`: 問題のテストクラスファイル
- `TreeNode.java`: （適用可能な場合）木構造に関連する問題のTreeNodeクラスファイル。

### UVa

解決済み: 568, 提出数: 1776

| Q1 | Q2 | Q3|
| ------------- | ------------- |-------------|
| 100: The 3n + 1 Problem | 101: The Blocks Problem | 102: Ecological Bin Packing |
| 103: Stacking Boxes | 104: Arbitrage | 105: The Skyline Problem |
| 106: Fermat's Last Theorem | 107: The Cat in the Hat | 108: Maximum Sum |
| 110: Meta-Loopless Sorts | 111: History Grading | 112: Tree Summing |
| 113: Power of Cryptography | 116: Unidirectional TSP | 118: Mutant Flatworld Explorers |
| 119: Greedy Gift Givers | 120: Stacks of Flapjacks | 122: Trees on the Level |
| 123: Searching Quickly | 124: Following Orders | 127: "Accordian" Patience |
| 128: Software CRC | 129: Krypton Factor | 131: The Domino Effect |
| 133: The Dole Queue | 136: Ugly Numbers | 138: Street Numbers |
| 140: Bandwidth | 146: ID Codes | 147: Dollars |
| 151: Power Crisis | 152: Tree's a Crowd | 156: Ananagrams |
| 160: Factors and Factorials | 167: The Sultan's Successors | 185: Roman Numerals |
| 190: Circle Through Three Points | 193: Graph Coloring | 195: Anagram |
| 196: Spreadsheet | 197: Orbiting Satellites | 200: Rare Order |
| 201: Squares | 202: Repeating Decimals | 208: Firetruck |
| 210: Determining Periods | 211: The Domino Effect | 213: Message Decoding |
| 216: Getting in Line | 221: Partitioning Polygon | 225: Golomb Rulers |
| 227: Puzzle | 230: Borrowers | 231: Testing the CATCHER |
| 247: Calling Circles | 253: Cube painting | 256: Quirksome Squares |
| 260: Il Gioco dell'X | 264: Count on Cantor | 272: TEX Quotes |
| 278: Chess | 280: Vertex | 291: The House Of Santa Claus |
| 294: Divisors | 297: Quadtrees | 299: Train Swapping |
| 301: Transportation | 305: Joseph | 307: Sticks |
| 315: Network | 317: Power Transmission | 324: Factorial Frequencies |
| 327: Evaluating Simple C Expressions | 331: Mapping the Swaps | 336: A Node Too Far |
| 340: Master-Mind Hints | 343: What Base Is This? | 344: Roman Digititis |
| 348: Optimal Array Multiplication Sequence | 350: Pseudo-Random Numbers | 352: The Seasonal War |
| 353: Pesky Palindromes | 357: Let Me Count The Ways | 369: Combinations |
| 371: Ackermann Functions | 374: Big Mod | 375: Inscribed Circles and Isosceles Triangles |
| 378: Intersecting Lines | 382: Perfection | 386: Perfect Cubes |
| 387: Repeated Substitution with Sed | 389: Basically Speaking | 392: Polynomial Showdown |
| 400: Unix ls | 401: Palindromes | 406: Prime Cuts |
| 408: Uniform Generator | 409: Excuses, Excuses! | 412: Pi |
| 414: Machined Surfaces | 417: Word Index | 424: Integer Inquiry |
| 429: Word Transformation | 437: The Tower of Babylon | 438: The Circumference of the Circle |
| 439: Knight Moves | 440: Eeny Meeny Moo | 441: Lotto |
| 442: Matrix Chain Multiplication | 443: Humble Numbers | 444: Encoder and Decoder |
| 445: Marvelous Mazes | 446: Kibbles `n' Bits `n' Bits `n' Bits | 455: Periodic Strings |
| 457: Linear Cellular Automata | 458: The Decoder | 459: Graph Connectivity |
| 465: Overflow | 469: Wetlands of Florida | 476: Points in Figures: Rectangles |
| 477: Points in Figures: Rectangles and Circles | 478: Points in Figures: Rectangles, Circles, Triangles | 481: What Goes Up |
| 482: Permutation Arrays | 483: Word Scramble | 484: The Department of Redundancy Department |
| 488: Triangle Wave | 489: Hangman Judge | 490: Rotating Sentences |
| 492: Pig-Latin | 494: Kindergarten Counting Game | 495: Fibonacci Freeze |
| 496: Simply Subsets | 497: Strategic Defense Initiative | 499: What's The Frequency, Kenneth? |
| 507: Jill Rides Again | 509: Just the Facts | 512: Taiwan Railway |
| 514: Rails | 524: Prime Ring Problem | 530: Binomial Showdown |
| 531: Compromise | 532: Dungeon Master | 534: Frogger |
| 536: Tree Recovery | 537: Railroads | 539: The Settlers of Catan |
| 540: Team Queue | 541: Error Correction | 543: Goldbach's Conjecture |
| 544: Heavy Cargo | 548: Tree | 550: Multiplying by Rotation |
| 558: Wormholes | 562: Dividing coins | 567: Risk |
| 568: Just the Facts | 572: Oil Deposits | 573: The Snail |
| 574: Sum It Up | 575: Skew Binary | 576: Haiku Review |
| 579: Clock Hands | 583: Prime Factors | 591: Box of Bricks |
| 594: One Little, Two Little, Three Little Endians | 612: DNA Sorting | 621: Secret Research |
| 623: 500! | 624: CD | 637: Booklet Printing |
| 639: Don't Get Rooked | 640: Self Numbers | 644: Immediate Decodability |
| 657: The die is cast | 661: Blowing Fuses | 673: Parentheses Balance |
| 674: Coin Change | 679: Dropping Balls | 686: Goldbach's Conjecture (II) |
| 694: The Collatz Sequence | 696: How Many Knights | 699: The Falling Leaves |
| 705: Slash Maze | 706: LC-Display | 712: S-Trees |
| 713: Adding Reversed Numbers | 714: Copying Books | 725: Division |
| 727: Equation | 729: The Hamming Distance Problem | 748: Exponentiation |
| 750: 8 Queens Chess Problem | 755: 487--3279 | 784: Maze Exploration |
| 793: Network Connections | 796: Critical Links | 815: Flooded! |
| 818: Job Matching | 820: Internet Bandwidth | 821: Page Hopping |
| 834: Continued Fractions | 836: Largest Submatrix | 839: Not so Mobile |
| 846: Steps | 847: A Multiplication Game | 900: Brick Wall Patterns |
| 913: Joana and the Odd Numbers | 924: Spreading The News | 929: Number Maze |
| 948: Fibonaccimal Base | 993: Product of digits | 1124: Celebrity jeopardy |
| 1149: Dangerous Dive | 1152: 4 Values whose Sum is 0 | 1203: Argus |
| 1225: Digit Counting | 1230: MODEX | 1237: Expert Enough? |
| 1260: Sales | 1339: Ancient Cipher | 1368: DNA Consensus String |
| 1374: Power Transmission | 1451: Ghostbusters 2 | 1471: Dangerous Dive |
| 1583: Digital Roots | 1584: Mathematics | 1585: Score |
| 1586: Molar Mass | 1587: Box | 1588: War |
| 1589: Partitioning | 1590: Elevator | 1592: Transmission |
| 1593: Pipes | 1594: Diamond | 1595: One Liner |
| 1604: Jumping Champion | 1605: Fibonacci Sum | 1606: Candy |
| 1607: Kaprekar Numbers | 1608: Random Walk | 1609: Look-and-say sequence |
| 10000: Longest Paths | 10003: Cutting Sticks | 10004: Bicoloring |
| 10006: Carmichael Numbers | 10008: What's Cryptanalysis? | 10010: Where's Waldorf? |
| 10012: How Big Is It? | 10013: Super long sums | 10014: Simple Base Conversion |
| 10018: Reverse and Add | 10019: Funny Encryption Method | 10025: The Game of MasterMind |
| 10026: Shoemaker's Problem | 10033: Billiard | 10034: Freckles |
| 10035: Primary Arithmetic | 10036: Divisibility | 10038: Jolly Jumpers |
| 10041: Vito's Family | 10042: Smith Numbers | 10047: The Monocycle |
| 10048: Audiophobia | 10050: Hartals | 10054: The Necklace |
| 10055: Hashmat the Brave Warrior | 10056: What is the Probability? | 10061: How to solve the cryptarithm? |
| 10062: Tell me the frequencies! | 10066: The Twin Towers | 10067: Playing with Wheels |
| 10070: Leap Year or Not Leap Year and ... | 10071: Back to High School Physics | 10074: Take the Land |
| 10077: The Stern-Brocot Number System | 10079: Pizza Cutting | 10082: WERTYU |
| 10098: Generating Fast | 10099: The Tourist Guide | 10101: Bangla Numbers |
| 10102: The path in the colored field | 10104: Euclid Problem | 10105: Polynomial Coefficients |
| 10106: Product | 10107: What is the Median? | 10110: Light, more light |
| 10112: Myacron Lifetime Achievement Award | 10114: Loansome Car Buyer | 10115: Automatic Editing |
| 10116: Robot Motion | 10123: Snowball Fight! | 10125: Sumsets |
| 10127: On a Diet | 10129: Play on Words | 10130: SuperSale |
| 10131: Is Bigger Smarter? | 10137: The Trip | 10139: Factovisors |
| 10140: Prime Distance | 10141: Request for Proposal | 10152: ShellSort |
| 10160: Servicing Stations | 10161: Ant on a Chessboard | 10167: Birthday Cake |
| 10168: Summation of Four Primes | 10170: The Hotel with Infinite Rooms | 10177: Magic Square Palindromes |
| 10179: Irreducible Basic Fractions | 10183: How many Fibs? | 10189: Minesweeper |
| 10190: Divide, But Not Quite Conquer! | 10191: Longest Nap | 10192: Vacation |
| 10193: All You Need Is Love | 10194: Football (aka Soccer) | 10195: The Knights Of The Round Table |
| 10198: Counting | 10199: Tourist Guide | 10205: Stack 'em Up |
| 10209: Is This Integration? | 10219: Find the ways! | 10220: I Love Big Numbers! |
| 10221: Two-Three Move | 10222: Decode the Message | 10226: Hardwood Species |
| 10229: Modular Fibonacci | 10235: Simply Emirp | 10242: Fourth Point !! |
| 10245: The Closest Pair Problem | 10250: The Other Two Trees | 10252: Common Permutation |
| 10258: Contest Scoreboard | 10260: Soundex | 10267: Graphical Editor |
| 10276: Hanoi Tower Troubles Again! | 10281: Average Speed | 10282: Babelfish |
| 10285: Longest Run on a Snowboard | 10286: Trouble with a Pentagon | 10295: Hay Points |
| 10298: Power Strings | 10299: Relatives | 10300: Ecological Premium |
| 10302: Summation of Polynomials | 10305: Ordering Tasks | 10310: Dog and Gopher |
| 10323: Factorial! You Must be Kidding!!! | 10324: Zeros and Ones | 10327: Flip Sort |
| 10334: Ray Through Glasses | 10336: Rank the Languages | 10338: Mischievous Children |
| 10340: All in All | 10341: Solve It | 10344: 23 out of 5 |
| 10346: Peter's Smokes | 10347: Medians | 10361: Automatic Poetry |
| 10369: Arctic Network | 10370: Above Average | 10387: Billiard Balls |
| 10391: Compound Words | 10392: Factoring Large Numbers | 10394: Twin Primes |
| 10397: Connect the Campus | 10405: Longest Common Subsequence | 10409: Die Game |
| 10420: List of Conquests | 10424: Love Calculator | 10432: Warehouse |
| 10450: World Cup Noise | 10452: Marcus | 10465: Homer Simpson |
| 10469: To Carry or not to Carry | 10473: Climbing Trees | 10474: The Candyman Can |
| 10487: Closest Sums | 10494: If We Were a Child Again | 10496: Collecting Beepers |
| 10499: Big Big Real Numbers | 10515: Power Sum | 10523: Very Easy !!! |
| 10530: Guessing Game | 10533: Digit Primes | 10534: Wavio Sequence |
| 10550: Combination Lock | 10557: XYZZY | 10562: Undraw the Trees |
| 10579: Fibonacci Numbers | 10583: Ubiquitous Religions | 10591: Happy Numbers |
| 10596: Deep Down Below | 10600: ACM Contest and Blackout | 10603: The Experimental Library |
| 10608: Friends | 10611: The Playboy Chimp | 10616: Divisible Group Sums |
| 10653: Bombs! NO they are Mines!! | 10656: Maximum Sum (II) | 10664: Luggage |
| 10673: Play with Floor and Ceil | 10679: I Love Strings!! | 10684: The jackpot |
| 10696: f91 | 10699: Count the factors | 10703: Free spots |
| 10719: Quirky Quantifiers | 10763: Foreign Exchange | 10773: Back to Intermediate Math |
| 10783: Odd Sum | 10784: Diagonal | 10785: Speed limit |
| 10789: Primo Words | 10790: How many points of intersection? | 10810: Ultra-QuickSort |
| 10812: Beat the Spread! | 10815: Andy's First Dictionary | 10878: Decode the tape |
| 10879: Maximum Sum (II) | 10905: Children's Game | 10911: Forming Quiz Teams |
| 10916: Factstone Benchmark | 10921: Find the Telephone | 10922: 2520 |
| 10924: Simple Minded Hashing | 10929: You can say 11 | 10931: Parity |
| 10935: Throwing cards away I | 10940: Throwing cards away II | 10943: How do you add? |
| 10945: Mother bear | 10948: The primary problem | 10954: Add All |
| 10963: The Swallowing Ground | 10970: Big Chocolate | 10976: Fractions Again?! |
| 10986: Sending email | 11000: Bee | 11044: Searching for Nessy |
| 11054: Wine trading in Gergovia | 11057: Exact Sum | 11059: Maximum Product |
| 11060: Beverages | 11085: Back to the 8-Queens | 11093: Just Finish it up |
| 11094: Continents | 11111: Generalized Matrioshkas | 11134: Fabled Rooks |
| 11137: Triple Fat Ladies | 11150: Cola | 11151: Longest Palindrome |
| 11152: Colourful Flowers | 11172: Relational Operator | 11185: Ternary |
| 11192: No Problem! | 11205: The broken pedometer | 11212: Editing a Book |
| 11214: Aladdin and the Flying Carpet | 11219: How Old Are You? | 11231: Black and white painting |
| 11234: Expressions | 11235: Frequent Values | 11244: Counting Stars |
| 11286: Conformity | 11292: Dragon of Loowater | 11332: Summing Digits |
| 11340: Newspaper | 11349: Symmetric Matrix | 11362: Phone List |
| 11364: Parking | 11369: Shopaholic | 11388: GCD LCM |
| 11389: The Bus Driver Problem | 11417: GCD | 11428: Cubes |
| 11450: Wedding Shopping | 11455: Behold my quadrangle | 11461: Square Numbers |
| 11462: Age Sort | 11479: Is this the easiest problem? | 11494: Queen |
| 11498: Division of Nlogonia | 11503: Virtual Friends | 11504: Dominos |
| 11530: SMS Typing | 11541: Decoding | 11547: Automatic Answer |
| 11559: Event Planning | 11565: Simple Equations | 11572: Unique Snowflakes |
| 11577: Letter Frequency | 11586: Train Tracks | 11608: No Problem! |
| 11614: Etruscan Warriors Never Play Chess | 11624: Fire! | 11631: Dark roads |
| 11636: Hello World! | 11650: Mirror Clock | 11661: Airport |
| 11677: Alarm Clock | 11679: Sub-prime | 11689: Soda Surpler |
| 11713: Abstract Names | 11715: Car | 11716: Digital Fortress |
| 11723: Numbering Roads | 11727: Cost Cutting | 11729: Commando War |
| 11734: Big Number of Teams will Solve This | 11743: Credit Check | 11764: Jumping Mario |
| 11777: Automate the Grades | 11799: Horror Dash | 11805: Bafana Bafana |
| 11809: Floating Point Numbers | 11827: Maximum GCD | 11831: Sticker Collector Robot |
| 11849: CD | 11854: Egypt | 11875: Brick Game |
| 11877: The Coco-Cola Store | 11879: Multiple of 17 | 11900: Boiled Eggs |
| 11933: Splitting Numbers | 11934: Magic Formula | 11936: The Lazy Lumberjacks |
| 11942: Lumberjack Sequencing | 11953: Battleships | 11984: A Change in Thermal Unit |
| 11988: Broken Keyboard (a.k.a. Beiju Text) | 11991: Easy Problem from Rujia Liu? | 11995: I Can Guess the Data Structure! |
| 12015: Google is Feeling Lucky | 12032: The Monkey and the Oiled Bamboo | 12096: The SetStack Computer |
| 12100: Printer Queue | 12107: One-Two-Three | 12108: Extraordinarily Tired Students |
| 12113: Sum of Different Primes | 12149: Feynman | 12157: Tariff Plan |
| 12174: Assemble | 12219: Searching Quickly | 12250: Language Detection |
| 12279: Emoogle Balance | 12289: One-Two-Three | 12325: Exact Change |
| 12333: Where is the Marble? | 12372: Packing for Holiday | 12403: Save Setu |
| 12405: Scarecrow | 12412: A Problem of Miscommunication | 12455: Bars |
| 12468: Zapping | 12478: Hardest Problem Ever (easy) | 12502: Three Families |
| 12503: Robot Instructions | 12504: Updating a Dictionary | 12545: Bits and Pieces |
| 12554: A Child’s Play | 12558: Cycle Finding | 12569: Sale |
| 12577: Hajj-e-Akbar | 12578: 10:6:2 | 12627: Error Correction |
| 12646: Majority Decision | 12657: Boxes in a Line |

### Codeforces

| Q1 | Q2 | Q3|
| ------------- | ------------- |-------------|
| 1003A: Polycarp's Pockets | 1030A: In Search of an Easy Problem | 1077A: Frog Jumping |
| 1092B: Teams Forming | 1095A: Repeating Cipher | 1097A: Gennady and a Card Game |
| 110A: Nearly Lucky Number | 112A: Petya and Strings | 1154A: Restoring Three Numbers |
| 115A: Party | 116A: Tram | 1183A: Nearest Interesting Number |
| 1186A: Vus the Cossack and a Contest | 118A: String Task | 1196A: Three Piles of Candies |
| 119A: Epic Game | 1206B: Make Product Equal One | 1220A: Cards |
| 122A: Lucky Division | 1234A: Equalize Prices Again | 124A: The Number of Positions |
| 1256A: Payment Without Change | 1283A: Minutes Before the New Year | 1285A: Mezo Playing Zoma |
| 1294A: Collecting Coins | 1294C: Product of Three Numbers | 1296A: Array with Odd Sum |
| 1296B: Food Buying | 1303A: Erasing Zeroes | 1304A: Two Rabbits |
| 1311A: Add Odd or Subtract Even | 1312A: Two Regular Polygons | 131A: cAPS lOCK |
| 1324A: Yet Another Tetris Problem | 1324B: Yet Another Palindrome Problem | 1324C: Frog Jumps |
| 1325A: EhAb AnD gCd | 1325B: CopyCopyCopyCopyCopy | 1326A: Bad Ugly Numbers |
| 1326B: Maximums | 1327A: Sum of Odd Integers | 1328A: Divisibility Problem |
| 1328B: K-th Beautiful String | 1328C: Ternary XOR | 1333A: Little Artem |
| 1334B: Middle Class | 1335A: Candies and Two Sisters | 1335B: Fair Division |
| 1335C: Hidden Word | 1335D: Anti-Sudoku | 1337A: Ichihime and Triangle |
| 1337B: Kana and Dragon Quest game | 1339A: Filling Diamonds | 1339B: Sorted Adjacent Differences |
| 133A: HQ9+ | 1341A: Nastya and Rice | 1342A: Road To Zero |
| 1342B: Binary Period | 1343A: Candies | 1343B: Balanced Array |
| 1343C: Alternating Subsequence | 1345A: Hilbert's Hotel | 1345B: Card Constructions |
| 1348A: Phoenix and Balance | 1350A: Orac and Factors | 1352A: Sum of Round Numbers |
| 1352B: Same Parity Summands | 1352C: K-th Not Divisible by n | 1353A: Most Unstable Array |
| 1353B: Number of Apartments | 1353C: Board Moves | 1354A: Alarm Clock |
| 1354B: Ternary String | 1355A: Sequence with Digits | 1355B: Young Explorers |
| 1358A: Park Lighting | 1358B: Maria Breaks the Self-isolation | 1359A: Berland Poker |