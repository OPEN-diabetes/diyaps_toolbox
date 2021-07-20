# DIYAPS Toolbox

The DIYAPS (Do-it-yourself Artificial Pancreas) Toolbox provides a set of functions for working with the data which can be extracted from AndroidAPS, Loop (iOS) and OpenAPS systems. 
The following table provides an overview of all the data items which can be calculated using this module. Each of the functions is explained in detail below: 

<br/><br/>



|   Data Item                                        |   Description                                                                                                                                                     |   Function                                                                                       |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
|   Days of data donated                             |   The period of time contained in the donated data based on the earliest and latest timestamp                                                                     |   calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")                                |
|   Mean sensor glucose                              |   Mean of all sensor glucose values in the Entries file                                                                                                           |   calculate_glucose_mean(glucose_values)                                                         |
|   Standard deviation of sensor glucose             |   Standard deviation of all sensor glucose values in the Entries file                                                                                             |   calculate_glucose_sd(glucose_values)                                                           |
|   Coefficient of Variation of sensor glucose       |   Coefficient of variation of all sensor glucose values in the Entries file                                                                                       |   calculate_glucose_cov(glucose_values)                                                          |
|   Glucose Managment Indicator                      |   Function for estimating the HbA1c value based on mean sensor glucose, as proposed by [1].                                                                       |   calculate_gmi(glucose_values)                                                                  |
|   % Time in Range                                  |   The time spent within the optimal range (by default set to 70 and 180 mg/dL) as a percentage                                                                    |   calculate_time_in_range(glucose_values, lower= 70, upper= 180)                                 |
|   % Time below Range                               |   Calculates the time spent below a certain threshold value (default = 70 mg/dL)                                                                                  |   calculate_time_below_range(glucose_values, lower = 70)                                         |
|   % Time above Range                               |   Calculates the time spent above a certain threshold value  (default= 180 mg/dL)                                                                                 |   calculate_time_above_range(glucose_values, upper = 180)                                        |
|   Number of hypoglcemic episodes per day           |   The mean number of hypoglycemic episodes per day. This function considers how often the blood glucose level   dropped below the threshold (default = 70 mg/dL)  |   calculate_hypos_per_day(glucose_values, date, lower= 70, date_format = "%Y-%m-%d-%H:%M:%S")    |
|   Number of hyperglycemic episodes per day         |   The mean number of hyperglycemic episodes per day. This function considers how often the blood glucose level rose above the threshold (default = 180 mg/dL)     |   calculate_hypers_per_day(glucose_values, date, upper= 180, date_format = "%Y-%m-%d-%H:%M:%S")  |
|   Percentage of persistent hypoglcemic episodes    |   The amount of hypoglycemic episodes that persisted for longer than 2 hours, as a percentage of all hypoglycemic episodes                                        |   calculate_persistent_hypo(glucose_values, lower= 70)                                           |
|   Percentage of persistent hyperglcemic episodes   |   The amount of hyperglycemic episodes that persisted for longer than 4 hours, as a percentage of all hypoglycemic episodes                                       |   calculate_persistent_hyper(glucose_values, upper = 180)                                        |
|   Percentage of overtreated hypoglcemic episodes   |   The percentage of hypoglycemic episodes that resulted in subsequent hyperglycemia within 2 hours                                                                |   calculate_overtreated_hypo(glucose_values, lower= 70, upper = 180)                             |
|   Percentage of overtreated hyperglcemic episodes  |   The percentage of hyperglycemic episodes that resulted in subsequent hypoglycemia within 4 hours                                                                |   calculate_overtreated_hyper(glucose_values, upper= 180, lower = 70)                            |
|   Number of meal boluses per day                   |   The mean number of meal boluses per day                                                                                                                         |   calculate_meal_bolus_per_day(treatment_df, date_format = "%Y-%m-%d-%H:%M:%S")                  |
|   Number of correction boluses per day             |   The mean number of correction boluses per day                                                                                                                   |   calculate_correction_bolus_per_day(treatment_df, date_format = "%Y-%m-%d-%H:%M:%S")            |
|   Grams of carbohydrates per day                   |   The mean number of carbohydrates entered into the system per day                                                                                                |   calculate_carbs_per_day(treatment_df, date_format = "%Y-%m-%d-%H:%M:%S")                       |
|   Units of correction insulin per day              |   The mean number of insulin units administered by the system as a correction bolus per day                                                                       |   calculate_correction_units_per_day(treatment_df, date_format = "%Y-%m-%d-%H:%M:%S")            |
|   Grams of carbs per meal                          |   The mean number of carbohydrates per meal bolus                                                                                                                 |   calculate_carbs_per_bolus(treatment_df)                                                        |
|   Units of insulin per correction dose             |   The mean number of insulin units per correction bolus                                                                                                           |   calculate_correction_units_per_day(treatment_df, date_format = "%Y-%m-%d-%H:%M:%S")            |

---
<br/><br/>
## Installation 

```
pip install diyaps_toolbox
```



---
[1]: Richard M. Bergenstal, Roy W. Beck, Kelly L. Close, George Grunberger, David B. Sacks, Aaron Kowalski, Adam S. Brown, Lutz Heinemann, Grazia Aleppo, Donna B. Ryan, Tonya D. Riddlesworth, and William T. Cefalu. “Glucose Management Indica- tor (GMI): A New Term for Estimating A1C From Continuous Glucose Monitoring”. In: Diabetes Care 41.11 (Sept. 2018), pages 2275–2280. doi: 10.2337/dc18-1581. url: https://doi.org/10.2337/dc18-1581.
