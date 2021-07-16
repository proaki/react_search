import React, {Component} from 'react';
import {DataSearch, ReactiveBase, ReactiveList, ResultList, SelectedFilters} from '@appbaseio/reactivesearch';
import './App.css';

const { ResultListWrapper } = ReactiveList;

class App extends Component {
    render() {
        return (
            <div className="main-container">
                <ReactiveBase
                    app="steam-search"
                    url="http://52.142.54.111:9200"
                >
                    <DataSearch
                        componentId="title"
                        dataField={["ResponseName"]}
                        queryFormat="and"
                    />
                    <SelectedFilters/>
                    <ReactiveList
                        componentId="resultLists"
                        dataField="ResponseName"
                        size={10}
                        pagination={true}
                        react={{
                            "and": ["title"]
                        }}
                    >
                        {({data}) => (
                            <ResultListWrapper>
                                {
                                    data.map(item => (
                                        <ResultList key={item._id}
                                                    href={`https://store.steampowered.com/app/${item.ResponseID}`}>
                                            <ResultList.Image src={item.HeaderImage}/>
                                            <ResultList.Content>
                                                <ResultList.Title
                                                    dangerouslySetInnerHTML={{
                                                        __html: item.ResponseName
                                                    }}
                                                />
                                                <ResultList.Description>
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