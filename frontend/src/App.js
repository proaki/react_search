import React, {useState} from 'react';
import {DataSearch, ReactiveBase, ReactiveList, ResultList, SelectedFilters, SingleRange, RangeSlider, MultiDataList, DateRange} from '@appbaseio/reactivesearch';
import './SteamSearch.css';
import reactStringReplace from "react-string-replace";
import 校長 from "./img/zoomロン２.jpg";

const ItemList = ["http://localhost:4000"];
const regExp = /(https?:\/\/\S+)/g;


const { ResultListWrapper } = ReactiveList;

const App = () => {
    const [isClicked, setIsClicked] = useState(false);
    const [message, setMessage] = useState("🔬Show Filters");
    // const [linked, setLinked] = useState();

    
      const handleClick = () => {        
        setIsClicked(!isClicked)
        setMessage(isClicked ? "🔬 Show Filters" : "🎮 Show Games")     
      };

    //   const handleClick2 = () => {        
    //       setLinked("./chat-bot/chat-bot/src/App.jsx")
    //   }
        
        return (
            <div className="main-container">
                <ReactiveBase
                    app="steam-search"
                    url="http://52.142.54.111:9200"
                    theme={
                        {
                            typography: {
                                fontFamily: 'Arial, Helvetica, sans-serif',
                                fontSize: '16px',
                            },
                            colors: {
                                titleColor: '#c7d5e0',
                                textColor: '#c7d5e0',
                                backgroundColor: '#212121',
                                primaryColor: '#CC9900',
                            }
                        }
                    }
                >
                    <DataSearch
                        componentId="title"
                        dataField={["ResponseName"]}
                        queryFormat="and"
                        placeholder="enter search term"
                        showIcon={false}
                        title="Steam Search"
                        className="data-search"
                        innerClass={{
                            input: 'input',
                            list: 'list',
                        }}
                    />
                    <SelectedFilters/>

                    <div className="sub-container">
                            <div
                                className={
                                isClicked ? "left-bar-optional" : "left-bar"
                                }   
                            >
                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-pied-piper-alt" /> Genres{" "}
                                    </b>
                                </div>

                                <MultiDataList
                                    componentId="genres-list"

                                    dataField="Genre"
                                    
                                    className="genres-filter"
                                    size={100}
                                    queryFormat="or"
                                    selectAllLabel="All Genres"
                                    placeholder="Search for a genre"     
                                    react={{
                                        and: [
                                            "title",
                                            "date-filter",
                                            "RangeSlider",
                                            "price-list",
                                            "resultLists"
                                        ]
                                        }}                               
                                    data={[
                                        {
                                            label: "Action",
                                            value: "Action"
                                        },
                                        {
                                            label: "Adventure",
                                            value: "Adventure"
                                        },
                                        {
                                            label: "Casual",
                                            value: "Casual"
                                        },
                                        {
                                            label: "EarlyAccess",
                                            value: "EarlyAccess"
                                        },
                                        {
                                            label: "FreeToPlay",
                                            value: "FreeToPlay"
                                        },
                                        {
                                            label: "Indie",
                                            value: "Indie"
                                        },
                                        {
                                            label: "MassivelyMultiplayer",
                                            value: "MassivelyMultiplayer"
                                        },
                                        {
                                            label: "NonGame",
                                            value: "NonGame"
                                        },
                                        {
                                            label: "Racing",
                                            value: "Racing"
                                        },
                                        {
                                            label: "RPG",
                                            value: "RPG"
                                        },
                                        {
                                            label: "Simulation",
                                            value: "Simulation"
                                        },
                                        {
                                            label: "Sports",
                                            value: "Sports"
                                        },
                                        {
                                            label: "Strategy",
                                            value: "Strategy"
                                        },
                                    ]}
                                    showFilter={true}
                                    showCount={true}
                                    URLParams={false}
                                    innerClass={{
                                        label: "list-item",
                                        input: "input"
                                    }}
                                />  

                                <hr className="blue" />                             


                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-dollar" /> PriceFinal{" "}
                                    </b>
                                </div>
                                <SingleRange
                                    componentId="price-list"
                                    dataField="PriceFinal"
                                    className="price-filter"
                                    data={[
                                        { start: 0.00, end: 5.00, label: "~ $5" },
                                        { start: 5.00, end: 10.00, label: "$5 - $10" },
                                        { start: 10.00, end: 50.00, label: "$10 - $50" },
                                        { start: 50.00, end: 100.00, label: "$50 - $100" },
                                        { start: 100.00, end: 500.00, label: "$100 ~" }
                                    ]}
                                    showRadio={true}
                                    showFilter={true}
                                    URLParams={false}
                                    innerClass={{
                                        label: "price-label",
                                        radio: "price-radio"
                                    }}
                                />                                
                                <hr className="blue" />

                                <div className="filter-heading center">
                                    <b>
                                        <i className="fa fa-star" /> Reccomend
                                        (Only:100~1000👍)
                                    </b>
                                </div>
                                <RangeSlider
                                    componentId="RangeSlider"
                                    dataField="RecommendationCount"
                                    className="range-slider"
                                    range={{
                                        start: 100,
                                        end: 1000
                                    }}
                                    rangeLabels={{
                                        start: "Umm...",
                                        end: "So Good!"
                                    }}
                                    react={{
                                        and: [
                                            "title",
                                            "date-filter",
                                            "genres-list",
                                            "price-list",
                                            "resultLists",
                                        ]
                                    }}
                                    innerClass={{                                        
                                        label: "range-label"
                                    }}
                                />
                                <hr className="blue" />
                             
                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-calendar" /> Release Date{" "}
                                    </b>
                                </div>
                                <DateRange
                                    componentId="date-filter"
                                    dataField="ReleaseDate"
                                    className="datePicker"
                                />
                                <hr className="blue" />

                                <div className="filter-heading center">
                                    <b>
                                        {""}
                                        <i className="fa fa-pied-piper-alt" /> Chat-Bot{" "}
                                    </b>



                                    <div className="chat-box">
                                        {ItemList.map((item) => {
                                        return (
                                            <div>
                                                {reactStringReplace(item, regExp, (match, i) => (
                                                    <a className="a" href={match}>
                                                        <img className="src" src={校長} width="100" height="100"/>
                                                    </a>
                                                ))}
                                            </div>
                                        )
                                        })}
                                    </div>                                    

                                </div>                
                                

                            </div>

                            <div
                                className={
                                    isClicked ? "result-container-optional" : "result-container"
                                }
                            >                          
                                <ReactiveList
                                    defaultQuery={() => ({ track_total_hits: true })}
                                    componentId="resultLists"
                                    dataField="ResponseName"
                                    size={25}
                                    pagination={true}
                                    react={{
                                        "and": [
                                            "title",
                                            "price-list",
                                            "genres-list",
                                            "RangeSlider",
                                            "date-filter",
                                        ]
                                    }}
                                    sortOptions={[
                                            {label: "Best Match", dataField: "RecommendationCount", sortBy: "desc"},
                                            {label: "Lowest Price", dataField: "PriceInitial", sortBy: "asc"},
                                            {label: "Highest Price", dataField: "PriceInitial", sortBy: "desc"},
                                    ]}
                                    className="result-list"
                                    innerClass={{
                                        resultsInfo: "resultsInfo",
                                        resultStats: "resultStats",
                                    }}
                                >
                                    
                                    {({data}) => (
                                        <ResultListWrapper>
                                            {
                                                data.map(item => (
                                                    <ResultList key={item._id}
                                                                href={`https://store.steampowered.com/app/${item.ResponseID}`}
                                                                className="listItem"
                                                    >
                                                        <ResultList.Image className="image" src={item.HeaderImage}/>
                                                        <ResultList.Content>
                                                            <ResultList.Title
                                                                dangerouslySetInnerHTML={{
                                                                    __html: item.ResponseName
                                                                }}
                                                            />
                                                            <ResultList.Description>
                                                            <p className="releaseDate">{item.ReleaseDate}</p>
                                                            <p className="price">${item.PriceInitial}</p>
                                                            </ResultList.Description>
                                                        </ResultList.Content>
                                                    </ResultList>
                                                ))
                                            }
                                        </ResultListWrapper>
                                    )}
                                </ReactiveList>
                            </div>
                        <button
                            className="toggle-button"
                            onClick={handleClick}
                            >
                            {message}
                        </button>
                    </div>
                </ReactiveBase>
            </div>
        );
    }


export default App;