import { useState } from "react";

function StudentProfile() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [semester, setSemester] = useState("");

  return (
    <div>
      <h2>Student Profile</h2>

      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Semester"
        value={semester}
        onChange={(e) => setSemester(e.target.value)}
      />

      <h3>Name: {name}</h3>
      <h3>Email: {email}</h3>
      <h3>Semester: {semester}</h3>
    </div>
  );
}

export default StudentProfile;