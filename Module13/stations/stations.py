from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column, ForeignKey
import csv

def create_schema():
    meta = MetaData()

    station = Table(
        'stations', meta,
        Column('id', String, primary_key=True),
        Column('latitude', String),
        Column('longitude', String),
        Column('elevation', String),
        Column('name', String),
        Column('country', String),
        Column('state', String),
    )

    measure = Table(
        'measures', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('station_id', String, ForeignKey("stations.id"), nullable=False),
        Column('date', String),
        Column('precip', String),
        Column('tobs', String),
    )

    meta.create_all(engine)

    return station, measure


def load_data(conn, station, measure):
    stations_data = conn.execute('''SELECT count(*) FROM stations ''').fetchall()[0][0]
    if stations_data == 0:
        with open('clean_stations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Columns: {", ".join(row)}')
                    line_count += 1
                else:
                    print(row)
                    ins = station.insert().values(id=row[0], latitude=row[1], longitude=row[2],
                                                  elevation=row[3], name=row[4], country=row[5],
                                                  state=row[6])

                    conn = engine.connect()
                    result = conn.execute(ins)
                    line_count += 1

    measures_data = conn.execute('''SELECT count(*) FROM measures ''').fetchall()[0][0]
    if measures_data == 0:
        with open('clean_measure.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Columns: {", ".join(row)}')
                    line_count += 1
                else:
                    # print(row)
                    ins = measure.insert().values(station_id=row[0], date=row[1], precip=row[2],
                                                  tobs=row[3])

                    conn = engine.connect()
                    result = conn.execute(ins)
                    line_count += 1


if __name__ == "__main__":
    engine = create_engine('sqlite:///stations.db')
    conn = engine.connect()

    station, measure = create_schema()

    print(engine.table_names())
    print()

    load_data(conn, station, measure)

    result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
    for row in result:
        print(row)

    print()

    result = conn.execute("SELECT * FROM measures LIMIT 5").fetchall()
    for row in result:
        print(row)


    conn.close()
