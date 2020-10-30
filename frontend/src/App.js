import React, {useEffect, useState} from "react";
import {Table, Typography} from "@equinor/eds-core-react";
import './App.css';
import styled from "styled-components";
import { colors } from "./Colors";

const { Body, Cell, Head, Row } = Table;

function App() {
    const [data, setData] = useState([]);
    
    const weatherData = () =>
        //http://localhost:8000/nowcast
        //"https://backend-gathering-eris-prod.playground.radix.equinor.com/nowcast"
       fetch("https://backend-gathering-eris-prod.playground.radix.equinor.com/nowcast" )
               .then((response) => response.json());
    
    useEffect (()=> {
        weatherData().then((data) => setData(data.locations))
    },[]);
    
    
    console.log(data);
    
    return (
    <div className="App">
        <AppContent>
            <HeaderContainer>
                <Header>Please Dress</Header>
                <About>Check how to dress before you go to work.</About>
            </HeaderContainer>
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
                            Clothing
                        </Cell>
                    </Row>
                </Head>
                <Body>
                    {data.map((item)=> (
                        <Row key={item.location}>
                            <Cell> {item.location}</Cell>
                            <Cell>{item.air_temperature}</Cell>
                            <Cell> {item.precipitation_rate}</Cell>
                            <Cell>{item.wind_speed}</Cell>
                            <Cell> </Cell>
                            <Cell>{item.clothing}</Cell>
                        </Row>
                    ))}
                </Body>
            </Table>
        </AppContent>
    </div>
    );
}

const AppContent = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
  background: ${colors.ui.backgroundDefault};
`;

const HeaderContainer = styled.div`
   padding: 4rem;
   
`;

const Header = styled(Typography)`
   font-size: xxx-large;
   font-weight: 900;
   color: ${colors.infographic.substituteBlueOvercast}; 
   text-align: center;
`;

const About = styled(Typography)`
   padding-top: 1rem;
   font-size: 
`;

export default App;