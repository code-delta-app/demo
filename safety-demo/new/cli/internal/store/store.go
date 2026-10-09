package store

// Ticket is a single support request.
type Ticket struct {
	ID       int
	Subject  string
	Body     string
	Status   string
	Priority int
}

// TicketStore is an in-memory collection of tickets.
type TicketStore struct {
	tickets map[int]*Ticket
	nextID  int
}

// NewTicketStore returns an empty store.
func NewTicketStore() *TicketStore {
	return &TicketStore{tickets: make(map[int]*Ticket), nextID: 1}
}

// Add inserts a ticket and returns its id.
func (s *TicketStore) Add(subject, body string, priority int) int {
	id := s.nextID
	s.tickets[id] = &Ticket{ID: id, Subject: subject, Body: body, Status: "open", Priority: priority}
	s.nextID++
	return id
}

// Get returns a ticket by id.
func (s *TicketStore) Get(id int) (*Ticket, bool) {
	t, ok := s.tickets[id]
	return t, ok
}

// Close marks a ticket closed.
func (s *TicketStore) Close(id int) bool {
	if t, ok := s.tickets[id]; ok {
		t.Status = "closed"
		return true
	}
	return false
}

// ListOpen returns all open tickets.
func (s *TicketStore) ListOpen() []*Ticket {
	var out []*Ticket
	for _, t := range s.tickets {
		if t.Status == "open" {
			out = append(out, t)
		}
	}
	return out
}

// Seed loads a little demo data.
func (s *TicketStore) Seed() {
	s.Add("Login fails", "User cannot sign in after reset", 2)
	s.Add("Export broken", "CSV export returns empty file", 1)
	s.Add("Feature request", "Add dark mode to portal", 0)
}
