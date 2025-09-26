import { useState, useEffect } from "react";
import { HStack, Select, Button, Text } from "@chakra-ui/react";
import { getCrewList } from "../../endpoints/api";
import axios from "axios";

const DISPATCH_URL = "/api/crew/dispatch/";

export const CrewDispatch = ({ card, onDispatched }) => {
    const [crew, setCrew] = useState([]);
    const [crewNumber, setCrewNumber] = useState(card?.crew || "");
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const load = async () => {
            try {
                const data = await getCrewList();
                setCrew(Array.isArray(data) ? data : []);
            } catch (err) {
                console.error("Ошибка загрузки бригад", err);
            }
        };
        load();
    }, []);

    const handleDispatch = async () => {
        if (!crewNumber) {
            alert("Выберете бригаду");
            return;
        }
        setLoading(true);
        try {
            const response = await axios.post(
                DISPATCH_URL,
                { card_id: card.id, crew_number: crewNumber },
                { withCredentials: true }
            );
            if (response.data?.success) {
                alert(`Карта №${card.id} отправлена бригаде № ${crewNumber}`);
                onDispatched && onDispatched();
            }
        } catch (err) {
            console.error(err);
            alert("Ошибка отправки карты");
        } finally {
            setLoading(false);
        }
    };

    return (
        <HStack>
            <Select
                placeholder="Выбрать бригаду"
                value={crewNumber}
                onChange={(e) => setCrewNumber(e.target.value)}
                isDisabled={loading}
                w="200px"
            >
                {crew.map((c) => (
                    <option key={c.id} value={c.crew_number}>
                        Бригада № {c.crew_number}
                    </option>
                ))}
            </Select>
            <Button
                onClick={handleDispatch}
                isLoading={loading}
                isDisabled={!crewNumber}
            >
                Отправить бригаде
            </Button>
        </HStack>
    );
};
