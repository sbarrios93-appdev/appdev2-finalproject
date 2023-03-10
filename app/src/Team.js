import { Button, Card } from "flowbite-react";
import React from "react";
import { useNavigate } from "react-router-dom";
function Team({ team, game }) {
  const navigate = useNavigate();
  const side = team.side == 1 ? "Home" : "Away";

  return (
    <div className="flex flex-col pb-8">
      <div className="flex flex-row">
        <div className="font-bold text-3xl text-zinc-200 pb-4">{side}</div>
        <Button
          className="ml-4 mt-3"
          text="Join"
          onClick={() => {
            navigate(`/games/${game.id}`);
          }}
        >
          Join
        </Button>
      </div>
      <div className="">
        <div className="font-bold text-xl text-zinc-200 pb-5">Players</div>
        <div className="font-light text-zinc-200">
          {team.players.map((player) => (
            <Card className="bg-slate-800 border-t-red-50">
              <div className="flex flex-row">
                <div></div>
                <div className="font-bold text-lg text-zinc-200">
                  {player.first_name} {player.last_name}
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Team;
