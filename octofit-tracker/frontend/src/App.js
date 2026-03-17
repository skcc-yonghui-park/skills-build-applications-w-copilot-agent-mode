import { Navigate, NavLink, Route, Routes } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

const NAV_ITEMS = [
  { to: '/users', label: 'Users', element: <Users /> },
  { to: '/teams', label: 'Teams', element: <Teams /> },
  { to: '/activities', label: 'Activities', element: <Activities /> },
  { to: '/leaderboard', label: 'Leaderboard', element: <Leaderboard /> },
  { to: '/workouts', label: 'Workouts', element: <Workouts /> },
];

function App() {
  return (
    <div className="app-shell container py-4 py-md-5">
      <header className="card shadow-sm border-0 mb-4 app-header-card">
        <div className="card-body app-header-body">
          <div className="app-brand mb-3">
            <img
              src={`${process.env.PUBLIC_URL}/octofitapp-small.png`}
              alt="OctoFit"
              className="app-logo"
            />
            <div>
              <h1 className="display-6 mb-2 app-title">OctoFit Tracker</h1>
              <p className="text-secondary mb-0">OctoFit data dashboard powered by Django REST API.</p>
            </div>
          </div>
          <nav aria-label="Main navigation">
            <ul className="nav nav-pills app-nav gap-2">
              {NAV_ITEMS.map((item) => (
                <li key={item.to} className="nav-item">
                  <NavLink
                    to={item.to}
                    className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
                  >
                    {item.label}
                  </NavLink>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </header>

      <main className="pb-4">
        <Routes>
          <Route path="/" element={<Navigate to="/users" replace />} />
          {NAV_ITEMS.map((item) => (
            <Route key={item.to} path={item.to} element={item.element} />
          ))}
          <Route path="*" element={<Navigate to="/users" replace />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
