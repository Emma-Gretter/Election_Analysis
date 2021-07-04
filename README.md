# Election_Analysis

## Project Overview
An audit of a local congressional election was performed. 

1. Total number of votes was calculated.
2. A complete list of candidates who received votes was compiled.
3. The total number of votes each candidate received was tallied.
4. The percentage of votes that each candidate won was calculated. 
5. The winner of the election was calculated using popular vote.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary 
The analysis of the election showed that:
- There were 369,711 total votes cast.
- The candidates were:
  - Diana DeGette
  - Raymond Anthony Doane
  - Charles Casper Stockham
- The candidate results were:
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymond Anthony Doane received 3.1% of the vote and 11,606 votes.
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
  
## Challenge Overview
An audit of each county in a local congressional election was performed.

## Challenge Results
The analysis of the counties showed that:
- There were 369,711 total votes cast.
- The counties were:
  - Arapahoe
  - Denver
  - Jefferson
- The county results were:
  - Arapahoe collected 6.7% of the vote and 24,801 votes.
  - Denver collected 82.8% of the vote and 306,055 votes.
  - Jefferson collected 10.5% of the vote and 38,855 votes.
- The county with the highest voter turnout was:
  - Denver, which collected 82.8% of the vote and 306,055 votes.
## Challenge Summary
The script used for this election analysis can easily be modified to audit future elections. Simply change the source data input to use data from a different election (here "election_results.csv" could be changed to a different file to use any other data desired).

```file_to_load = os.path.join("resources", "election_results.csv")```

Other factors, such as party affiliation could be added to future analysis. If a fourth column which included voter party affiliation were added to the source data document, then a variable could be initialized like so:

```voter_party_affilialtion = row[3]```

Then voter turnout by party could be calculated, as well as percentage of vote per party and party with largest percentage of turnout.


