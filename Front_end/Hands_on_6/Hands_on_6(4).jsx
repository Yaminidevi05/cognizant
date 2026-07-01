function Header() {
  return (
    <header>
      <h1>Student Portal</h1>

      <nav>
        <Link to="/">Home</Link>{" "}
        <Link to="/courses">Courses</Link>{" "}
        <Link to="/profile">Profile</Link>
      </nav>
    </header>
  );
}

export default Header;