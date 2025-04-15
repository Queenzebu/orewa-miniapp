import { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Home, Activity, User, Wallet } from 'lucide-react';
import { motion } from 'framer-motion';
import Dashboard from '@/components/Dashboard';
import Mining from '@/components/Mining';
import Profile from '@/components/Profile';
import WalletConnect from '@/components/WalletConnect';
import NavIcon from '@/components/NavIcon';

export default function OrewaApp() {
  const [activeTab, setActiveTab] = useState('home');

  const tabs = {
    home: <Dashboard />,
    mining: <Mining />,
    profile: <Profile />,
    wallet: <WalletConnect />,
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f172a] to-[#1e293b] text-white flex flex-col">
      <header className="p-4 flex items-center justify-between">
        <img src="https://gateway.pinata.cloud/ipfs/bafkreia5mfs2nlcpv7tj5igdk7o6g524ginccbuzwz4rjb5rztjerncjvq" alt="OREWA Logo" className="h-10" />
        <h1 className="text-xl font-bold">OREWA</h1>
      </header>

      <motion.main
        className="flex-1 p-4"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
      >
        {tabs[activeTab]}
      </motion.main>

      <nav className="bg-[#0f172a] border-t border-slate-800 p-2 flex justify-around">
        <NavIcon icon={<Home />} label="Home" active={activeTab === 'home'} onClick={() => setActiveTab('home')} />
        <NavIcon icon={<Activity />} label="Mining" active={activeTab === 'mining'} onClick={() => setActiveTab('mining')} />
        <NavIcon icon={<User />} label="Profile" active={activeTab === 'profile'} onClick={() => setActiveTab('profile')} />
        <NavIcon icon={<Wallet />} label="Wallet" active={activeTab === 'wallet'} onClick={() => setActiveTab('wallet')} />
      </nav>
    </div>
  );
}
