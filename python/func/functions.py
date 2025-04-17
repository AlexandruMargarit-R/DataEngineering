def top_each(dataframe, filter_value):
    filtered_df = dataframe[dataframe["type"] == filter_value]
    filtered_df = filtered_df.drop(columns=["show_id", "cast", "country", "date_added"])
    return filtered_df
