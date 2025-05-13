from pyspark.sql import DataFrame

def get_products_with_categories(
    products_df : DataFrame,
    categories_df : DataFrame,
    product_category_df : DataFrame
) -> DataFrame:
    """
    Returns DataFrame with two columns:
    - product_name
    - category_name

    :param products_df: DataFrame (product_id, product_name)
    :param categories_df: DataFrame (category_id, category_name)
    :param product_category_df: DataFrame (product_id, category_id)
    :return: DataFrame (product_name, category_name)
    """

    product_category_with_names_df = product_category_df \
        .join(categories_df, on="category_id", how="left")

    result_df = products_df \
        .join(product_category_with_names_df, on="product_id", how="left") \
        .select("product_name", "category_name")

    return result_df