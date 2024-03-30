Pyspark project created for Big Data Programming course (Spring 2024).
_____________________________________________________________________________
Data Information:
Columns are: UserID, MovieID, Rating. "Rating" is the rating for the movie identified by MovieID.
The output file here is what results from running these scripts.
_____________________________________________________________________________
Algorithm Explanation:
1. Accumulate an rdd whose keys are users and values are a list of movies reviewed by that user
2. Accumulate an rdd whose keys are users and values are a list of movies positively reviewed by that user
3. Iterate through each user. For each user, iterate through all of the positively reviewed movies found in the rdd of positive reviews. If the movie in question is not already in the current user's list of recommendations and also not already reviewed by the user, then accumulate the movie into a list of recommendations for the user.
_____________________________________________________________________________
How to run each python file:
1. For simplicity, create a dataproc Linux VM environment (Google cloud has tools available).
2. Upload these files into the VM's root: input.txt, assignment8_part1.py, and assignment8_part2.py.
3. Type the following commands into the terminal:
   hdfs dfs -put input.txt input
   spark-submit [python file here]
5. Wait for the script to fully run until it successfully writes to output/output.txt.
6. Type the following command:
   hdfs dfs -getmerge output/* [name of output file].txt
8. This output text file will hold the output attached to this repository.
