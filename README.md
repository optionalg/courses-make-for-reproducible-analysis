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
He currently re-runs analyses with RStudio scripts,
but now that he's getting hundreds of new datasets each week,
he would like to re-run only the calculations he needs to.
This course will show him how to do that.

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

![Concept Map for Make](design/concept.svg)

<!-- -------------------------------------------------------------------------------- -->

## Step 4: What will the learner do along the way?

### Do Analysis By Hand

Run `bin/patient-total`, `bin/patient-average`, and `bin/scatter` by hand
to trace the calculations for one patient.

### Recalculate One Patient's Data

- Write a Make rule to run `bin/patient-total` to recreat the daily dosage file for one patient.
- Use `touch` to trigger execution.
- Add a new raw dosage file for that patient and check that the rule runs.

### Recalculate Dependent Files

- Add rules to regenerate `results/averages.csv` and `result/averages.png`.
- Use `touch` to check that programs only run when they need to.
- Trigger the whole execution chain by adding a new raw dosage file.

### Using Automatic Variables

- Rewrite existing rules using `$@`, `$^`, and `$<`.

### Creating a Tree of Dependencies

- Add a rule to regenerate `daily/AC1433.csv`.
- Modify the rule for `results/averages.csv` so that it is updated when it needs to be.
- Test using `touch` and by adding more data files.
- See what happens when a daily dosage file is *removed* (answer: nothing).

### Writing Pattern Rules

- Write a wildcard pattern rule to replace the separate rules for `AC1071` and `AC1433`.
- Test by adding more data files for each patient.
- Test again by adding an entirely new patient.

### Including All Dependencies

- Modify rules to re-run when their scripts change.

### Other Kinds of Rules

- Write a phony `clean` target.
- Write a phony `test` target.

### Using Macros

- Replace names of scripts with macros.

<!-- -------------------------------------------------------------------------------- -->

## Step 5: How are the concepts connected?

The chapter and lesson outline is:

- Simple Rules
  - What is Make?
  - What does a simple rule contain?
  - How does Make handle dependencies?
- Writing Better Rules
  - What are automatic variables?
  - What is a pattern rule?
  - What is a macro?
- Project Management
  - How can we use Make to manage projects?
  - How can we make execution depend on changes to scripts?

The datasets are:

- Dosage files.
- A Python script to generate random dosage files.

<!-- -------------------------------------------------------------------------------- -->

## Step 6: How will learners find the course and know if it's for them?

**Course Description**

Make is a tool that can keep track of which files depend on which
others, and update ones that have fallen out of date.  While it was
originally invented to help prorammers compile complex programs, data
analysts now use it to ensure that their work is reproducible.  This
lesson will introduce key elements of Make and show you how to use
them efficiently.

**Learning Objectives**

- Explain what Make is for and how it differs from using handwritten scripts.
- Identify the targets, dependencies, and actions of rules.
- Trace the execution order of rules in a short Makefile.
- Use automatic variables to shorten rules.
- Use wildcards to write pattern rules.
- Use macros and functions to make Makefiles more readable.
- Use Make to automate project management tasks.

**Prerequisites**

- Introduction to the Unix Shell for Data Scientists
