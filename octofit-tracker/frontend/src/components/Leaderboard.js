import { useEffect, useState } from 'react';

function Leaderboard() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [query, setQuery] = useState('');
  const [selectedItem, setSelectedItem] = useState(null);

  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespaceName
    ? `https://${codespaceName}-8000.app.github.dev/api/leaderboard/`
    : 'http://localhost:8000/api/leaderboard/';

  async function loadLeaderboard(signal) {
    try {
      setLoading(true);
      setError('');
      console.log('[Leaderboard] endpoint:', apiUrl);
      const response = await fetch(apiUrl, { signal });
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      const data = await response.json();
      console.log('[Leaderboard] fetched payload:', data);
      const normalizedItems = Array.isArray(data)
        ? data
        : Array.isArray(data?.results)
          ? data.results
          : [];
      setItems(normalizedItems);
    } catch (err) {
      if (err.name !== 'AbortError') {
        setError('Failed to load leaderboard.');
      }
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    const controller = new AbortController();
    loadLeaderboard(controller.signal);
    return () => controller.abort();
  }, [apiUrl]);

  const filteredItems = items.filter((item) => {
    if (!query.trim()) {
      return true;
    }
    const text = `${item.rank ?? ''} ${item.points ?? ''} ${item.user ?? ''} ${item.id ?? ''}`.toLowerCase();
    return text.includes(query.toLowerCase());
  });

  return (
    <section className="card shadow-sm border-0">
      <div className="card-body">
        <div className="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
          <h2 className="h4 mb-0">Leaderboard</h2>
          <div className="d-flex align-items-center gap-3">
            <a className="link-primary" href={apiUrl} target="_blank" rel="noreferrer">
              API endpoint
            </a>
            <button
              type="button"
              className="btn btn-primary btn-sm"
              onClick={() => loadLeaderboard()}
              disabled={loading}
            >
              Refresh
            </button>
          </div>
        </div>

        <form className="row g-2 mb-3" onSubmit={(event) => event.preventDefault()}>
          <div className="col-sm-8 col-md-6">
            <input
              type="text"
              className="form-control"
              placeholder="Search leaderboard by rank, user, or points"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
            />
          </div>
          <div className="col-auto">
            <button type="button" className="btn btn-outline-secondary" onClick={() => setQuery('')}>
              Clear
            </button>
          </div>
        </form>

        {error && <div className="alert alert-danger py-2">{error}</div>}

        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">User</th>
                <th scope="col">Rank</th>
                <th scope="col">Points</th>
                <th scope="col" className="text-end">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr>
                  <td colSpan="5" className="text-center py-4">
                    Loading...
                  </td>
                </tr>
              ) : filteredItems.length === 0 ? (
                <tr>
                  <td colSpan="5" className="text-center py-4">
                    No leaderboard data found.
                  </td>
                </tr>
              ) : (
                filteredItems.map((item) => (
                  <tr key={item.id}>
                    <td>{item.id}</td>
                    <td>{item.user}</td>
                    <td>{item.rank}</td>
                    <td>{item.points}</td>
                    <td className="text-end">
                      <button
                        type="button"
                        className="btn btn-outline-primary btn-sm"
                        onClick={() => setSelectedItem(item)}
                      >
                        View
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {selectedItem && (
        <>
          <div className="modal d-block" tabIndex="-1" role="dialog" onClick={() => setSelectedItem(null)}>
            <div className="modal-dialog modal-lg modal-dialog-centered" onClick={(event) => event.stopPropagation()}>
              <div className="modal-content">
                <div className="modal-header">
                  <h3 className="modal-title h5 mb-0">Leaderboard details</h3>
                  <button type="button" className="btn-close" onClick={() => setSelectedItem(null)} />
                </div>
                <div className="modal-body">
                  <pre className="bg-light rounded p-3 mb-0">{JSON.stringify(selectedItem, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setSelectedItem(null)}>
                    Close
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show" />
        </>
      )}
    </section>
  );
}

export default Leaderboard;
