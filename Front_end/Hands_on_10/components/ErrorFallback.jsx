function ErrorFallback() {
  return (
    <div
      style={{
        padding: "40px",
        textAlign: "center",
      }}
    >
      <h1>Something went wrong.</h1>

      <p>Please refresh the application.</p>
    </div>
  );
}

export default ErrorFallback;