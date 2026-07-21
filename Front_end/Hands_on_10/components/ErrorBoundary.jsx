import React from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      hasError: false,
    };
  }

  static getDerivedStateFromError() {
    return {
      hasError: true,
    };
  }

  componentDidCatch(error, info) {
    console.error(error);
    console.error(info);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ textAlign: "center", marginTop: "40px" }}>
          <h1>Something went wrong.</h1>
          <p>Please refresh the application.</p>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;