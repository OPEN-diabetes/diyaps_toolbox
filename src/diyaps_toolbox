import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re
import os


def calculate_glucose_mean(glucose_values):
    return data.mean()

def calculate_glucose_sd(glucose_values):
    return data.std()

def calculate_glucose_cov(glucose_values):
    return(data.std()/data.mean())

def calculate_gmi(glucose_values): 
    gmi = 3.31 + (0.02393 *  glucose_values.mean())
    return gmi

def calculate_time_in_range(glucose_values, lower= 70, upper= 180):
    count = 0
    for index, row in glucose_values.iteritems():
        if (glucose_values[index] < upper) & (glucose_values[index] > lower):
            count += 1
    tir = count / len(glucose_values)
    return tir

def calculate_time_below_range(glucose_values, lower = 70):
    count = 0
    for index, row in glucose_values.iteritems():
        if (glucose_values[index] < lower):
            count += 1
    hypo = count / len(df)
    return hypo

def calculate_time_above_range(glucose_values, upper = 180):
    count = 0
    for index, row in glucose_values.iteritems():
        if (glucose_values[index] > upper):
            count += 1
    hyper = count / len(df)
    return hyper

def calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S"):
    a = datetime.datetime.strptime(date.iloc[-1], date_format)
    b = datetime.datetime.strptime(date.iloc[0], date_format)
    delta = b - a
    return delta

def calculate_overtreated_hypo(glucose_values, lower= 70, upper = 180):
    count = 0
    overtreated = 0 
    i = 0 
    index = 0
    while index < len(glucose_values):
        if (glucose_values[index] < lower):
            count += 1
            i = index
            index += 24 # 2 hours later
            if index < len(df) and glucose_values[index]  > upper:
                while i < len(df) and i < index+18: #2 hours later  
                    overtreated += 1
                    i +=18 # break?
            else:
                i += 1
        else: 
            index += 1
    percentage_overtreated = (overtreated / count)
    return percentage_overtreated


def calculate_persistent_hypo(glucose_values, lower= 70):
    count = 0
    persistent = 0 
    i = 0 
    index = 0
    while index < len(df):
        if (glucose_values[index] < lower):
            count += 1
            i = index
            limit = index
            index += 6 # half an hour later
            if index < len(df) and glucose_values[index]  < lower:
                persistent +=1 
                while index < len(df) and glucose_values[index] < lower:
                    index += 1
        else: 
            index += 1
    percentage_persistent = (persistent /count)
    return percentage_persistent

def calculate_overtreated_hyper(glucose_values, upper= 180, lower = 70):
    count = 0
    overtreated = 0 
    i = 0 
    index = 0
    while index < len(glucose_values):
        if (glucose_values[index] > upper):
            count += 1
            i = index
            index += 24 # 2 hours later
            if index < len(df) and glucose_values[index]  < lower:
                while i < len(df) and i < index+18: #2 hours later  
                    overtreated += 1
                    i +=18 # break?
            else:
                i += 1
        else: 
            index += 1
    percentage_overtreated = (overtreated / count)
    return percentage_overtreated

def calculate_persistent_hyper(glucose_values, upper = 180):
    count = 0
    persistent = 0 
    i = 0 
    index = 0
    while index < len(df):
        if (glucose_values[index] > upper):
            count += 1
            i = index
            limit = index
            index += 24  # 2 hours later
            if index < len(df) and glucose_values[index]  > upper:
                persistent +=1 
                while index < len(df) and glucose_values[index] > upper:
                    index += 1
        else: 
            index += 1
    percentage_persistent = (persistent /count)
    return percentage_persistent

def calculate_hypos_per_day(glucose_values, date, lower= 70, date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    count = 0
    index = 0
    while index < len(df):
        if (glucose_values[index] < lower):
            count += 1
            index += 24 
        else: 
            index += 1
    return(count/days)


def calculate_hypers_per_day(glucose_values, date, upper= 180, date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    count = 0
    index = 0
    while index < len(df):
        if (glucose_values[index] > upper):
            count += 1
            index += 24 
        else: 
            index += 1
    return(count/days)

def calculate_meal_bolus_per_day(treatment_df ,date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    meal_bolus = df[df['eventType'] == 'Meal Bolus'].shape[0]
    return(meal_bolus/days)


def calculate_correction_bolus_per_day(treatment_df ,date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    correction_bolus = df[df['eventType'] == 'Correction Bolus'].shape[0]
    return(correction_bolus/days)


def calculate_carbs_per_day(treatment_df ,date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    carbs = df['carbs'].sum()
    return()


def calculate_correction_units_per_day(treatment_df ,date_format = "%Y-%m-%d-%H:%M:%S"):
    days = calculate_days_donated(date, date_format = "%Y-%m-%d-%H:%M:%S")
    correction_units = df['insulin'].sum()
    return(correction_units/days)

def calculate_carbs_per_bolus(treatment_df):
    meal_bolus = df[df['eventType'] == 'Meal Bolus'].shape[0]
    carbs = df['carbs'].sum()
    return(carbs/meal_bolus)


def calculate_correction_units_per_bolus(treatment_df):
    correction_bolus = df[df['eventType'] == 'Correction Bolus'].shape[0]
    correction_units = df['insulin'].sum()
    return (correction_units/correction_units)

