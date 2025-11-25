<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/ae0a4ac2-eba5-483a-9024-ea7b3684a888" />

# mPower Data Filtering and Preprocessing

This repository contains tools to process, clean, and filter the **mPower Parkinson's Disease dataset**. The pipeline extracts raw audio from Synapse cache structures and filters participants based on strictly defined clinical criteria for Machine Learning tasks.

## About the mPower Dataset

This project utilizes data from the **mPower study**, a clinical observational study of Parkinson's Disease (PD) conducted purely through an iPhone app interface. Launched in March 2015, the study used Apple's ResearchKit library to collect frequent sensor-based recordings and surveys from participants with and without PD.

The goal of the study was to evaluate the feasibility of remotely collecting frequent information about daily changes in symptom severity and sensitivity to medication.

### The Voice Activity Dataset

This repository specifically focuses on the **Voice Activity** portion of the mPower dataset.

* **The Task:** Participants were instructed to say "Aaaaah" into their microphone at a steady volume for up to 10 seconds.

* **The Data:** The activity recorded audio files for the 10 seconds of phonation as well as the 5-second countdown leading up to the task.

* **Medication States:** To track symptom fluctuation, participants with a professional diagnosis of PD were asked to perform tasks at three specific times:

  1. Immediately before taking their medication.

  2. After taking their medication (when feeling at their best).

  3. At another time.

## Project Structure

* `scripts/extract_raw_audio.py`: Flattens the nested Synapse cache structure (`.tmp` files) into a usable directory of audio files.

* `notebooks/mPower_filtering.ipynb`: Filters the dataset into "People with Parkinson's" (PwPD) and "Healthy Controls" (HC).

## Filtering Criteria

The filtering logic aligns with standard voice analysis protocols:

1. **Age Range:** 50–70 years old.

2. **Exclusions:** Participants with Depression, Anxiety, Schizophrenia, Bipolar disorder, Asthma, Stroke, or COPD are removed.

3. **Group Definitions:**

   * **PwPD:** Professional diagnosis = `True`, medication usage confirmed, no Deep Brain Stimulation (DBS).

   * **HC:** Professional diagnosis = `False`, explicitly states "I don't take Parkinson medications".

4. **Medication Timing:** For PwPD, only recordings taken "Immediately before medication" or "Another time" are kept (OFF state). "Just after medication" (ON state) is excluded.

5. **Uniqueness:** Ensures only one unique recording per participant (`healthCode`) is retained.

## Usage

1. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
2. **Extract Audio:**
   The raw data from Synapse is often downloaded into a nested cache structure (e.g., `data(.synapseCache)/.../*.tmp`). Run the extraction script to flatten this structure, rename the files to `.wav`, and organize them into a clean `data/` directory.

    ```bash
    python scripts/extract_raw_audio.py
    ```
3. **Run Notebook:**
Open the Jupyter notebook to perform the clinical cohort filtering (Age, Diagnosis, Medication) and generate the training/testing splits for your machine learning model.

    ```bash
    jupyter notebook notebooks/mPower_filtering.ipynb
    ```

## Data Access and Governance

**Note:** This repository **does not** contain the mPower dataset. Due to the sensitive nature of health data, the dataset is hosted on Synapse and is subject to strict governance to protect participant privacy.

To run the processing scripts in this repository, you must obtain the data directly from the [mPower Public Researcher Portal](https://www.synapse.org/mPower).

**Requirements for Access:**
Researchers interested in accessing the data must complete the following steps:

1. **Create a Synapse Account:** Register at [synapse.org](https://synapse.org).

2. **Profile Validation:** Have your User Profile validated by the Synapse Access and Compliance Team (ACT).

3. **Certification:** Become a Certified User by passing a short quiz on research ethics.

4. **Intended Data Use:** Submit a statement describing how you intend to use the data.

5. **Conditions for Use:** Agree to terms including a commitment not to re-identify participants and to keep data confidential.

Once approved, you can download the raw data (including audio files and demographic tables) to use as inputs for the preprocessing pipeline in this repository.

## Citations

If you use this dataset in your work, please cite the original mPower paper:

> Bot, B. M. et al. The mPower Study, Parkinson Disease Mobile Data Collected Using ResearchKit. Sci. Data 3:160011 doi: 10.1038/sdata.2016.11 (2016).

   
