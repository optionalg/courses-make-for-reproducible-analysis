# Make for Reproducible Analysis

<!-- -------------------------------------------------------------------------------- -->

## Step 1: Who is this lesson for?

### [Anya](https://github.com/datacamp/learner-profiles#anya)

<img alt="Anya" src="https://raw.githubusercontent.com/datacamp/learner-profiles/master/img/anya.png" height="150" width="150" />

Anya started using Make in her first C programming course twenty years ago,
but has never used it to automate data analysis.
This course will show her some new tricks and spark some new ideas.

### [Thanh](https://github.com/datacamp/learner-profiles#thanh)

<img alt="Thanh" src="https://raw.githubusercontent.com/datacamp/learner-profiles/master/img/thanh.png" height="150" width="150" />

Thanh has never seen Make before.
This course will show him how to re-run analyses when datasets or algorithms change.

<!-- -------------------------------------------------------------------------------- -->

## Step 2: How far will this lesson get its learners?

The directory `dosage` contains sub-directories whose names are patient IDs
like `AC1071` and `DN2249`.
Each sub-directory contains one or more CSV data files whose names are ISO-formatted dates
(e.g, `dosage/AC1071/2017-10-02.csv`)
that are formatted like this:

```
Time,Dosage (mg)
03:45,30
07:30,30
11:50,60
16:10,30
04:00,20
09:55,100
13:20,20
17:00,100
```

Another directory called `daily` contains one CSV file per patient with daily total dosages,
e.g. `daily/AC1071.csv` contains:

```
Date,Total Dosage (mg)
2017-10-02,1500
2017-10-09,1350
2017-10-16,1200
```

A third directory called `results` contains a single file called `averages.csv`
that records the average daily dose per patient with the duration in dates of the dosage period,
e.g.:

```
Patient ID,Dosage Duration,Average Daily Dosage (mg)
AC1071,61,1422.5
DN2249,55,1190.0
```

It also contains a scatter plot in `results/averages.png` that shows
the relationship between dosage duration and average daily dosage.

The directory `bin` contains three analysis scripts:

1. `bin/patient-total output-file file-1 file-2 ...` reads data from one or more raw dosage files
   (like those in `dosage/AC1071/2017-10-02.csv`)
   and re-creates that patient's total daily dosage file
   (like those in `daily/AC1071.csv`).
2. `bin/patient-average output-file file-1 file-2` reads one or more daily dosage files
   (like those in `daily/AC1071.csv`)
   and re-creates an average daily dosage file `results/averages.csv`.
3. `bin/scatter input-file output-file` reads an average daily dosage file like `results/averages.csv`
   and creates a scatter plot like `results/averages.png`.

New daily dosage files are being added to existing patient directories all the time,
and new patient directories are being created weekly.
Write a Makefile that correctly regenerates the two files in the `results` directory
every time any new data is added.
Do only those computations that are strictly required.

<!-- -------------------------------------------------------------------------------- -->

## Step 3: What will the learner's mental model be at the end of the lesson?

<em>

</em>

![Basic Make Concepts](img/make.png)

<!-- -------------------------------------------------------------------------------- -->

## Step 4: What will the learner do along the way?

FIXME

<!-- -------------------------------------------------------------------------------- -->

## Step 5: In what order will the learner do things?

The formative assessments in Step 4 (Formative Assessments) are already in order.

<!-- -------------------------------------------------------------------------------- -->

## Step 6: How are the exercises connected?

The chapter and lesson outline is:

- FIXME

The datasets are:

- FIXME

<!-- -------------------------------------------------------------------------------- -->

## Step 7: How will learners find the course and know if it's for them?

**Course Description**

Make is a tool that can keep track of which files depend on which
others, and update ones that have fallen out of date.  While it was
originally invented to help prorammers compile complex programs, data
analysts now use it to ensure that their work is reproducible.  This
lesson will introduce key elements of Make and show you how to use
them efficiently.

**Learning Objectives**

- FIXME

**Prerequisites**

- Introduction to the Unix Shell for Data Scientists
