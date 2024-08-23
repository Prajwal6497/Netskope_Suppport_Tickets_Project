import React, { useEffect, useState } from "react";
import axios from "axios";

const TicketsList = () => {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    // Fetch tickets from FastAPI endpoint
    axios.get("http://localhost:8000/tickets")
      .then(response => {
        setTickets(response.data);
      })
      .catch(error => {
        console.error("Error fetching tickets:", error);
      });
  }, []);

  return (
    <div>
      <h1>Support Tickets</h1>
      <ul>
        {tickets.map((ticket, index) => (
          <li key={index}>
            <h3>{ticket.name} ({ticket.email})</h3>
            <p>{ticket.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TicketsList;
