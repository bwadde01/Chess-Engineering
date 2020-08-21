# Chess-Engineering

![alt text](https://github.com/bwadde01/Chess-Engineering/blob/master/ForkImages958.jpg)

Being both a chess and ML/data science enthusiast, naturally I am interested in seeing the intersection between the two. In this repository I explore what data I could work with in this area, initially with the intention of creating a chess tactic identifier using computer vision (specifically for identifying scenarios where a player could fork an opponent's pieces). I quickly discovered that this would not be feasible, as the data seemed to be interpreted as just noise by the CNN model (so no learning was happening).

Further, I decided that the function of determining a tactic was better left to the available engines out there such as Stockfish. However, I still found the experience of collecting
data fruitful.

First, because I had decided to focus on identifying forks, I scraped the content from the puzzles listed on chess.com that were tagged as testing forks (https://www.chess.com/puzzles/). 

Then, from this content I extracted the FEN representation of each puzzles from the scraped content. 

And finally, after scraping the FEN representations of the board positions that tested forks, I uploaded the FEN to http://www.fen-to-image.com to download the image 
representation of the position.

I am deciding to leave this project for now, as I see a misalignment between the next steps and my current goal of working on more machine learning projects.  
