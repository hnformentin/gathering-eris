import {Table} from "@equinor/eds-core-react";
import './App.css';

const { Body, Cell, Head, Row } = Table;

const dummyData = [
    {"location": "Stavanger",
        "air_temperature": "10C",
        "percipitation_rate": "1mm",
        "wind_speed": "7m/s",
        "clothing": "allversjakke",
        "time_until_rain": "90",
        "next_1_hours": {
            "symbol_code": "Cloudy",
            "precipitation_amount": "0.0"
        },
        "reccomendation": "shorts"
    },
    {"location": "Trondheim",
        "air_temperature": "10C",
        "percipitation_rate": "1mm",
        "wind_speed": "7m/s",
        "clothing": "allversjakke",
        "time_until_rain": "90",
        "next_1_hours": {
            "symbol_code": "Cloudy",
            "precipitation_amount": "0.0"
        },
        "reccomendation": "allversjakke"},
];



function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Table>
                    <Head>
                        <Row>
                            <Cell as="th" scope="col" >
                                Location
                            </Cell>
                            <Cell as="th" scope="col" >
                                Temp.
                            </Cell>
                            <Cell as="th" scope="col" >
                                Persip.
                            </Cell>
                            <Cell as="th" scope="col" >
                                Wind Speed
                            </Cell>
                            <Cell as="th" scope="col" >
                                Next Hour
                            </Cell>
                            <Cell as="th" scope="col" >
                                Reccomendation
                            </Cell>
                        </Row>
                    </Head>
                    <Body>
                        {dummyData.map((item)=> (
                            <Row key={item.location}>
                                <Cell> {item.location}</Cell>
                                <Cell>{item.air_temperature}</Cell>
                                <Cell> {item.percipitation_rate}</Cell>
                                <Cell>{item.wind_speed}</Cell>
                                <Cell> {item.next_1_hours.precipitation_amount}</Cell>
                                <Cell>{item.reccomendation}</Cell>
                            </Row>
                        ))}
                    </Body>
                </Table>
            </header>
        </div>
    );
}

export default App;