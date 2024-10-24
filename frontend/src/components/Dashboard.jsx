import { useState, useEffect } from "react";
import axios from "axios";
import "../style/Dashboard.css";

const Dashboard = ({ onLogout }) => {
  const [credentials, setCredentials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [applicationFilter, setApplicationFilter] = useState("");
  const [usernameFilter, setUsernameFilter] = useState("");
  const [urlFilter, setURLFilter] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [inputPage, setInputPage] = useState("");

  // Fetch credentials with optional filters
  const fetchCredentials = async (page = 1) => {
    setLoading(true);
    try {
      const token = localStorage.getItem("token");
      let url = "http://127.0.0.1:8000/api/credentials/";

      // Add query parameters for filtering
      const params = {
        page: page, // Pagination parameter
      };
      if (applicationFilter) params.application = applicationFilter;
      if (usernameFilter) params.username = usernameFilter;
      if (urlFilter) params.url = urlFilter;

      const response = await axios.get(url, {
        headers: { Authorization: `Bearer ${token}` },
        params: params, // Send filters as query parameters
      });

      // Set data and pagination info
      setCredentials(response.data.results);
      setCurrentPage(page);
      setTotalPages(Math.ceil(response.data.count / 10)); // Assuming each page has 10 items
    } catch (error) {
      console.error("Failed to fetch credentials:", error);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchCredentials(currentPage);
  }, []);

  // Handler functions for the filter inputs
  const handleApplicationFilterChange = (event) => {
    setApplicationFilter(event.target.value);
  };

  const handleUsernameFilterChange = (event) => {
    setUsernameFilter(event.target.value);
  };

  const handleURLFilterChange = (event) => {
    setURLFilter(event.target.value);
  };

  // Apply filters by making a backend request
  const applyFilters = () => {
    fetchCredentials(1); // Reset to the first page when applying new filters
  };

  // Pagination handler
  const goToNextPage = () => {
    if (currentPage < totalPages) {
      fetchCredentials(currentPage + 1);
    }
  };

  const goToPreviousPage = () => {
    if (currentPage > 1) {
      fetchCredentials(currentPage - 1);
    }
  };

  // Handle direct page input navigation
  const handlePageInputChange = (event) => {
    setInputPage(event.target.value);
  };

  const goToPage = () => {
    const pageNumber = parseInt(inputPage, 10);
    if (pageNumber >= 1 && pageNumber <= totalPages) {
      fetchCredentials(pageNumber);
      setInputPage(""); // Clear the input after navigation
    } else {
      alert("Invalid page number");
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      goToPage();
    }
  };

  return (
    <div className="dashboard">
      <nav className="navbar">
        <h2>Credentials Dashboard</h2>
        <button onClick={onLogout}>Logout</button>
      </nav>

      <div className="filter-container">
        <input
          type="text"
          placeholder="Filter by Application"
          value={applicationFilter}
          onChange={handleApplicationFilterChange}
        />
        <input
          type="text"
          placeholder="Filter by Username"
          value={usernameFilter}
          onChange={handleUsernameFilterChange}
        />
        <input
          type="text"
          placeholder="Filter by URL"
          value={urlFilter}
          onChange={handleURLFilterChange}
        />
        <button onClick={applyFilters}>Apply Filters</button>
      </div>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <table>
            <thead>
              <tr>
                <th>Application</th>
                <th>Username</th>
                <th>Password</th>
                <th>URL</th>
              </tr>
            </thead>
            <tbody>
              {credentials.map((credential, index) => (
                <tr key={index}>
                  <td>{credential.application}</td>
                  <td>{credential.username}</td>
                  <td>{credential.password}</td>
                  <td>
                    <a
                      href={credential.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      {credential.url}
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="pagination">
            <button onClick={goToPreviousPage} disabled={currentPage === 1}>
              Previous
            </button>
            <span>
              Page {currentPage} of {totalPages}
            </span>
            <button
              onClick={goToNextPage}
              disabled={currentPage === totalPages}
            >
              Next
            </button>
            <input
              type="text"
              value={inputPage}
              onChange={handlePageInputChange}
              onKeyPress={handleKeyPress}
              placeholder="Go to page..."
            />
            <button onClick={goToPage}>Go</button>
          </div>
        </>
      )}
    </div>
  );
};

export default Dashboard;
