import React, {Component} from 'react';
import {DataSearch, ReactiveBase, ReactiveList, ResultList, SelectedFilters, MultiList, SingleRange, RangeSlider, MultiDataList, DateRange} from '@appbaseio/reactivesearch';
import './SteamSearch.css';

const { ResultListWrapper } = ReactiveList;

class App extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          isClicked: false,
          message: "🔬Show Filters"
        };
      }
    
      handleClick() {
        this.setState({
          isClicked: !this.state.isClicked,
          message: this.state.isClicked ? "🔬 Show Filters" : "🎬 Show Movies"
        });
      }

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

                    <div className="sub-container">
                            <div
                                className={
                                this.state.isClicked ? "left-bar-optional" : "left-bar"
                                }   
                            >
                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-pied-piper-alt" /> Genres{" "}
                                    </b>
                                </div>
                                
                                <MultiList
                                    componentId="genres-list"
                                    dataField="genres_data.raw"
                                    className="genres-filter"
                                    size={20}
                                    sortBy="asc"
                                    queryFormat="or"
                                    selectAllLabel="All Genres"
                                    showCheckbox={true}
                                    showCount={true}
                                    showSearch={true}
                                    placeholder="Search for a Genre"
                                    react={{          
                                        and: [
                                            "mainSearch",
                                            "results",
                                            "date-filter",
                                            "RangeSlider",
                                            "language-list",
                                            "revenue-list"
                                        ]
                                    }}          
                                    showFilter={true}
                                    filterLabel="Genre"
                                    URLParams={false} 
                                    innerClass={{ 
                                        label: "list-item",
                                        input: "list-input"
                                    }}                    
                                />
                                <hr className="blue" />


                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-dollar" /> Revenue{" "}
                                    </b>
                                </div>
                                <SingleRange
                                    componentId="revenue-list"
                                    dataField="ran_revenue"
                                    className="revenue-filter"
                                    data={[
                                    { start: 0, end: 1000, label: "< 1M" },
                                    { start: 1000, end: 10000, label: "1M-10M" },
                                    { start: 10000, end: 500000, label: "10M-500M" },
                                    { start: 500000, end: 1000000, label: "500M-1B" },
                                    { start: 1000000, end: 10000000, label: "> 1B" }
                                    ]}
                                    showRadio={true}
                                    showFilter={true}
                                    filterLabel="Revenue"
                                    URLParams={false}
                                    innerClass={{
                                    label: "revenue-label",
                                    radio: "revenue-radio"
                                    }}
                                />                                
                                <hr className="blue" />

                                <div className="filter-heading center">
                                    <b>
                                        <i className="fa fa-star" /> Ratings
                                    </b>
                                </div>
                                <RangeSlider
                                    componentId="RangeSlider"
                                    dataField="vote_average"
                                    className="review-filter"
                                    range={{
                                    start: 0,
                                    end: 10
                                    }}
                                    rangeLabels={{
                                    start: "0",
                                    end: "10"
                                    }}
                                    react={{
                                    and: [
                                        "mainSearch",
                                        "results",
                                        "language-list",
                                        "date-Filter",
                                        "genres-list",
                                        "revenue-list"
                                    ]
                                    }}
                                />
                                <hr className="blue" />

                                <div className="filter-heading center">
                                    <b>
                                        {" "}
                                        <i className="fa fa-language" /> Languages{" "}
                                    </b>
                                </div>
                                <MultiDataList
                                    componentId="language-list"
                                    dataField="original_language.raw"
                                    className="language-filter"
                                    size={100}
                                    sortBy="asc"
                                    queryFormat="or"
                                    selectAllLabel="All Languages"
                                    showCheckbox={true}
                                    showSearch={true}
                                    placeholder="Search for a language"
                                    react={{
                                    and: [
                                        "mainSearch",
                                        "results",
                                        "date-filter",
                                        "RangeSlider",
                                        "genres-list",
                                        "revenue-list"
                                    ]
                                    }}
                                    data={[
                                    {
                                        label: "English",
                                        value: "English"
                                    },
                                    {
                                        label: "Chinese",
                                        value: "Chinese"
                                    },
                                    {
                                        label: "Turkish",
                                        value: "Turkish"
                                    },
                                    {
                                        label: "Swedish",
                                        value: "Swedish"
                                    },
                                    {
                                        label: "Russian",
                                        value: "Russian"
                                    },
                                    {
                                        label: "Portuguese",
                                        value: "Portuguese"
                                    },
                                    {
                                        label: "Korean",
                                        value: "Korean"
                                    },
                                    {
                                        label: "Japanese",
                                        value: "Japanese"
                                    },
                                    {
                                        label: "Italian",
                                        value: "Italian"
                                    },
                                    {
                                        label: "Hindi",
                                        value: "Hindi"
                                    },
                                    {
                                        label: "French",
                                        value: "French"
                                    },
                                    {
                                        label: "Finnish",
                                        value: "Finnish"
                                    },
                                    {
                                        label: "Spanish",
                                        value: "Spanish"
                                    },
                                    {
                                        label: "Deutsch",
                                        value: "Deutsch"
                                    }
                                    ]}
                                    showFilter={true}
                                    filterLabel="Language"
                                    URLParams={false}
                                    innerClass={{
                                    label: "list-item",
                                    input: "list-input"
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
                                    dataField="release_date"
                                    className="datePicker"
                                />



                            </div>

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
                    <button
                        className="toggle-button"
                        onClick={this.handleClick.bind(this)}
                        >
                        {this.state.message}
                    </button>
                    </div>
                </ReactiveBase>
            </div>
        );
    }
}

export default App;