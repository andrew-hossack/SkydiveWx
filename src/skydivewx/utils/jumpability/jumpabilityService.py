from utils.metar import Metar


def _convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split("/")
        except ValueError:
            return None
        try:
            leading, num = num.split(" ")
        except ValueError:
            return float(num) / float(denom)
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))


def getJumpability(metar: Metar.Metar, forecastData: dict) -> dict:
    ##### Thresholds #####
    wind_limit_mph = 15
    gust_limit_mph = wind_limit_mph + 5
    visibility_limit_miles = 5
    temperature_max_limit_f = 90
    temperature_min_limit_f = 32
    ##### Penalties #####
    temperature_penalty = 30
    visibility_penalty = 30
    overcast_penalty = 30
    #####################

    jump_score = 100  # Set the initial score to 100
    sub_results = {
        "results": {"jump_score": jump_score, "penalties": {}},
        "limits": {
            "thresholds": {
                "wind_limit_mph": wind_limit_mph,
                "gust_limit_mph": gust_limit_mph,
                "visibility_limit_miles": visibility_limit_miles,
                "temperature_max_limit_f": temperature_max_limit_f,
                "temperature_min_limit_f": temperature_min_limit_f,
            },
            "penalties": {
                "temperature_penalty": temperature_penalty,
                "visibility_penalty": visibility_penalty,
                "overcast_penalty": overcast_penalty,
            },
        },
    }

    # Handle probability of precipitation from forecastData
    precip_subtractor = forecastData["probabilityOfPrecipitation"]["value"]
    jump_score -= precip_subtractor
    sub_results["results"]["penalties"]["precipitation"] = precip_subtractor

    # Handle temperature from forecastData
    if (
        forecastData["temperature"] > temperature_max_limit_f
        or forecastData["temperature"] < temperature_min_limit_f
    ):  # Arbitrary thresholds, adjust as needed
        jump_score -= temperature_penalty
        sub_results["results"]["penalties"]["temperature"] = temperature_penalty

    # Handle wind from metar
    wind_metar = int(
        metar.wind_speed.value("KT")
    )  # Convert wind from metar to integer in knots
    wind_subtractor = (
        max(0, wind_metar - wind_limit_mph) * 2
    )  # Decrease score for wind above limit
    jump_score -= wind_subtractor
    sub_results["results"]["penalties"]["wind"] = wind_subtractor

    # Handle gust from metar
    if metar.wind_gust:
        wind_gust = int(metar.wind_gust.value("KT"))
        gust_subtractor = (
            max(0, wind_gust - gust_limit_mph) * 2
        )  # Decrease score for wind gust above limit
        jump_score -= gust_subtractor
        sub_results["results"]["penalties"]["gust"] = gust_subtractor

    # Handle weather from metar
    if any(["SN" in condition for condition in metar.weather]) or any(
        ["RA" in condition for condition in metar.weather]
    ):
        jump_score = 0
        sub_results["results"]["penalties"]["snowRain"] = 100

    # Handle visibility from metar
    try:
        visibility_miles = int(str(metar.visibility("SM").split(" ")[0]))
    except ValueError:
        # Visibility is a float (1/2 mile vis for example)
        visibility_miles = _convert_to_float(str(metar.visibility("SM").split(" ")[0]))
    else:
        # Visibility sometimes is "missing"
        visibility_miles = None
    if visibility_miles and (
        visibility_miles < visibility_limit_miles
    ):  # Arbitrary threshold, adjust as needed
        jump_score -= visibility_penalty
        sub_results["results"]["penalties"]["visibility"] = visibility_penalty

    # Handle sky condition from metar
    if "OVC" or "BKN" in metar.sky():
        jump_score -= overcast_penalty
        sub_results["results"]["penalties"]["overcast"] = overcast_penalty

    # Ensure score stays within 0-100 range
    jump_score = max(0, min(100, jump_score))
    sub_results["results"]["jump_score"] = round(jump_score)
    return sub_results


def describeJumpability(jump_score: int) -> str:
    if jump_score <= 0:
        return "Unsuitable for Skydiving"
    elif 0 < jump_score <= 20:
        return "Skydiving Not Advised"
    elif 20 < jump_score <= 40:
        return "Sub-optimal Jump Conditions"
    elif 40 < jump_score <= 60:
        return "Adequate Jump Conditions"
    elif 60 < jump_score <= 80:
        return "Favorable Jump Conditions"
    elif 80 < jump_score < 100:
        return "Optimal Jump Conditions"
    else:  # 100
        return "Ideal Jump Conditions"
