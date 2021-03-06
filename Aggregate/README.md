## Shell Scripts:

- runyear.sh: To get the total word count for each year, run wcYearMapper.py and wcYearReducer.py 
by hadoop streaming.

- run.sh: In this shell script, we get total count of each year from last step(runyear.sh). 
Then run wcByYearMapper and wcByYearReducer to get each word count per year.
Then, use wcAvgByYearMapper.py, we divide each word count per year by the total count of that year.

## Python Scripts:

Firstly, data comes from : http://stateoftheunion.onetwothree.net/texts/index.html

- YearMapper.py, YearReducer.py: Mapper and Reducer python scripts to get the total words count in each year.
    - Input: original html files and STOPWORDS.TXT
    - Output: FILE "yearcount": \<year, count\>


- wcByYearMapper.py, wcByYearReducer.py: Count words appearance in each year
    - Input: original html files and STOPWORDS.TXT
    - Output: FILE \<word, year, count\>

- wcAvgByYearMapper.py: Compute the average use of a word per year. AVG_USER = (word_count_per_year/total_count_per_year)
    - Input: FILE yearcount and FILE \<word, year, count\>
    - Output: FILE \<word,year,avg_use\>

- allcountMapper.py: To get popular words, compute total count of a word over all the years.
    - Input: FILE <word, year, count>
    - Output: FILE \<word, count\>

- popularMapper.py: In order to draw the graph of popular words counts over all years, compute the top words by counts. 
So I switch the word and count position. Then MapRed will shuffle and sort the <key, value> tuple by count integer.
    - Input: FILE \<word, count\>
    - Output: FILE \<count, word\>

- maxminMapper.py: To compute the maximum and minimum times of a word over all years.
    - Input: FILE \<word, count\>
    - Output: FILE max_word, max_count
        min_word, min_count


## Input and Intermediate Output:

- test-allcount: result of allcountMapper.py

- test-avg: result of wcAvgByYearMapper.py

- test-count: result of wcByYearMapper.py and wcByYearReducer.py

- test-maxmin: result of maxminMapper.py

- test-pop: result of popularMapper.py

- test-year: result of YearMapper.py and YearReducer.py
