import {
  TableContainer,
  Table,
  Thead,
  Th,
  Tr,
  Tbody,
  Td,
  Button,
} from "@chakra-ui/react";

import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { colorBackgroundStatus } from "../constants/table-fields";
import { getOnlineDoctors } from "../endpoints/api";
import { DoctorChoice } from "./fields/doctor-choice";

export const CardTable = ({ columns, cards, onCardUpdate }) => {
  const navigator = useNavigate();
  const [doctors, setDoctors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchDoctors = async () => {
      setIsLoading(true);
      try {
        const res = await getOnlineDoctors();
        setDoctors(res);
      } catch (e) {
        console.error("Ошибка загрузки врачей:", e);
      } finally {
        setIsLoading(false);
      }
    };
    fetchDoctors();
  }, []);

//   const handleDoctorAssigned = () => {
//     // Если нужно обновить список карт после назначения врача
//     if (onCardUpdate) {
//       onCardUpdate();
//     }
//   };

  return (
    <TableContainer>
      <Table variant="simple">
        <Thead>
          <Tr>
            {columns.map((col) => {
              return <Th key={col.field}>{col.label} </Th>;
            })}
          </Tr>
        </Thead>
        <Tbody>
          {cards.map((card) => {
            const bgColor = colorBackgroundStatus[card.status] || "grey.100";
            return (
              <Tr
                bg={bgColor}
                key={card.id}
                _hover={{ bg: "gray.100", cursor: "pointer" }}
              >
                {/* Ячейки с данными */}
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.id}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.patient.last_name}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.patient.first_name}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.patient.surname}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.patient.date_of_birth}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.address}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.cause}
                </Td>
                <Td>
                  {card.doctor ? (
                    `${card.doctor.first_name} ${card.doctor.last_name}`
                  ) : (
                    <DoctorChoice
                      doctors={doctors}
                      card={card}
                      onDoctorAssigned={onCardUpdate}
                    />
                  )}
                </Td>
                <Td onClick={() => navigator(`/cards/${card.id}`)}>
                  {card.status}
                </Td>

                {/* Отдельная ячейка для кнопки редактирования */}
                <Td>
                  <Button
                    onClick={(e) => {
                      e.stopPropagation();
                      navigator(`/cards/${card.id}/update`);
                    }}
                  >
                    Редактировать
                  </Button>
                </Td>
              </Tr>
            );
          })}
        </Tbody>
      </Table>
    </TableContainer>
  );
};
