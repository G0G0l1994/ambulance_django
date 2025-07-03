import axios from "axios";
import React from "react";

class App extends React.Component {
  state = { details: [] };

  componentDidMount() {
    let data;
    axios
      .get("http://127.0.0.1:8000/api/users/")
      .then((res) => {
        data = res.data;
        this.setState({
          details: data,
        });
      })
      .catch((err) => {});
  }
  render() {
    return (
      <div>
        <header> Data Generaded from Django</header>
        <hr></hr>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <div class='users'>
              <h2>
                {id}
                {output.username}
              </h2>
              <h3>{output.role}</h3>
            </div>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
