import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import movieData from './movies.json';

function fetchAndFormat(temp) {
  return temp.map((elem) => {
    const dateStr = elem.releaseDate;
    const dateObj = new Date(dateStr)
    elem.dateObj = dateObj
    return elem
  })
}

function Filter(props) {
  return (
    <div>
      <button onClick={props.onClick}>
      {props.description}
      </button>
    </div>
  );
}

class Board extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      data: fetchAndFormat(movieData),
    }
    this.baseState = this.state
  }


  handleClickDate() {
    console.log("click date")
    const temp = this.state.data.slice()
    temp.sort((a, b) => {
      return new Date(b.dateObj) - new Date(a.dateObj);
    })

    this.setState({data: temp});
  }

  handleClickName() {
    console.log("click name")
    const temp = this.state.data.slice()

    temp.sort(function(a, b) {
      var nameA = a.title.toUpperCase()
      var nameB = b.title.toUpperCase()
      if (nameA < nameB) {
        return -1
      }
      if (nameA > nameB) {
        return 1
      }
      // names must be equal
      return 0
    })

    this.setState({data: temp});
  }

  handleClickClear() {
    console.log("click clear")
    this.setState(this.baseState)
  }

  renderMovie(elem) {
    return (
      <Movie 
        data={elem}
      />
    );
  }

  render() {
    return (
        <div>
          <div className="flex-container">
            <Filter 
              onClick={() => this.handleClickDate()}
              description="Sort by date"
            />
            <Filter 
               onClick={() => this.handleClickName()} 
               description="Sort by name"
            />
            <Filter 
               onClick={() => this.handleClickClear()}
               description="Clear filter and sort"
            />
          </div>
          <div className="flex-container">

            {this.state.data.map((elem) => this.renderMovie(elem))}
            <Placeholder />
            <Placeholder />
          </div>
        </div>
    );
  }
}

function Movie(props) {
  return (
    <div className="card">
      <Image src={props.data.image}/>
      <h1>{props.data.title}</h1>
      <Release date={props.data.releaseDate}/>
      <Review rate={props.data.rating}/>
    </div>
  );
}

function Release(props) {
  return (
    <p>{props.date}</p>
  );
}

function Review(props) {
  return (
    <div>
      <Rate rate={props.rate} />
      <Star rate={props.rate} />
    </div>
  );
}

function Rate(props) {
  return (
    <p>Rating {props.rate}</p>
  );
}

function Star(props) {
  var stars = [];
  for (var i = 0; i < 5; i++) {
    if (i < props.rate) stars.push(<span className="blue-text">&#9733;</span>);
    else stars.push(<span className="grey-text">&#9733;</span>);
  }
  return stars
}

function Image(props) {
  return (
    <img src={props.src}/>
  );
}

function Placeholder(props) {
  return (
    <div className="card no-bg">
    </div>
  );
}

// ========================================

ReactDOM.render(
  <Board />,
  document.getElementById('root')
);
