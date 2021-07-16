import React, {Component} from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import {DataSearch, ReactiveBase, ReactiveList, ResultList, SelectedFilters} from '@appbaseio/reactivesearch';
import './App.css';
import './SteamSearch.css'
import SignIn from './signin';


const { ResultListWrapper } = ReactiveList;

class App extends Component {
    render() {
        
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
                                primaryColor: '#2B475E',
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
                    <ReactiveList
                        componentId="resultLists"
                        dataField="ResponseName"
                        size={25}
                        pagination={true}
                        react={{
                            "and": ["title"]
                        }}
                        sortOptions={[
                                {label: "Best Match", dataField: "_score", sortBy: "desc"},
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
                                                  <p className="headerImage">${item.HeaderImage}</p>
                                                  <p className="releaseDate">${item.ReleaseDate}</p>
                                                  <p className="price">$${item.PriceInitial}</p>
                                                </ResultList.Description>
                                            </ResultList.Content>
                                        </ResultList>
                                    ))
                                }
                            </ResultListWrapper>
                        )}
                    </ReactiveList>
                </ReactiveBase>
            </div>
        );
    }
}

export default App;