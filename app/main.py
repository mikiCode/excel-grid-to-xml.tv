import uvicorn
from fastapi import FastAPI, File, HTTPException
import pandas as pd
from grid.schema import excel_columns


# create app
app = FastAPI()


# create post endpoint
@app.post("/grid/upload/")
async def grid_upload(file: bytes = File(...)):
    # check if file is an excel file by failing to read it with pandas
    try:
        df = pd.read_excel(file)
    except ValueError:
        raise HTTPException(415, detail="Invalid file type")

    # choosing columns to keep, hardcoded in schema.py
    try:
        df = df[excel_columns]
    except KeyError:
        raise HTTPException(400, detail="Invalid column names in excel file")
    # convert datetime columns to strings with format required by xmltv - yyyymmddhhmmss
    df["Start Time"] = pd.to_datetime(
        df["Start Time"], format="%H:%M:%S", errors="coerce"
    ).dt.strftime("%H%M%S")
    df["Date"] = df["Date"].dt.strftime("%Y%m%d")
    df["Duration"] = pd.to_datetime(
        df["Duration"], format="%H:%M:%S", errors="coerce"
    ).dt.strftime("%H:%M:%S")
    # concatenating columns df["Date"] and df["Start Time"] to get column with format yyyymmddhhmmss
    df["programme start"] = df["Date"] + df["Start Time"]
    # create a column for the end time of the programme, no other way to retain 24h handling without hardcoding it
    df["programme end"] = (
        pd.to_datetime(df["programme start"], format="%Y%m%d%H%M%S")
        + pd.to_timedelta(df["Duration"])
    ).dt.strftime("%Y%m%d%H%M%S")

    # export pandas dataframe to json with channel and date range in filename
    grid_name = (
        df["Channel Name"].iloc[0]
        + " "
        + str(df["Date"].iloc[0])[:10]
        + " "
        + str(df["Date"].iloc[-1])[:10]
    )
    df.to_json(f"{grid_name}.json", orient="records", indent=2)
    return {"message": "File uploaded successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
