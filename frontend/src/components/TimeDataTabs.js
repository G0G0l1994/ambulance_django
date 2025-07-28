import { useEffect, useState } from "react";
import { HStack, Input, Text, VStack, Grid, GridItem } from "@chakra-ui/react";

const TimeDataTab = ({ time, onRefSave }) => {
  const [localData, setLocalData] = useState(time);

  useEffect(() => {
    setLocalData(time);
  }, [time]);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({ ...prev, [field]: value }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData;
    }
  }, [localData, onRefSave]);
  return (
    <Grid gap={5} templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={1}>
        <HStack>
          <Text>Время приёма:</Text>
          <Input
            value={new Date(localData.time_of_receipt || "").toLocaleTimeString(
              "ru-ru"
            )}
            onChange={(e) => handleChange("time_of_receipt", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время передачи:</Text>
          <Input
            value={new Date(
              localData.transmission_time || " "
            ).toLocaleTimeString("ru-ru")}
            onChange={(e) => handleChange("transmission_time", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время принятия бригадой:</Text>
          <Input
            value={new Date(localData.departure_time || " ").toLocaleTimeString(
              "ru-ru"
            )}
            onChange={(e) => handleChange("departure_time", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время прибытия:</Text>
          <Input
            value={new Date(localData.arrival_time || " ").toLocaleTimeString(
              "ru-ru"
            )}
            onChange={(e) => handleChange("arrival_time", e.target.value)}
          />
        </HStack>
      </GridItem>
      <GridItem>
        <HStack>
          <Text>Начало госпитализации:</Text>
          <Input
            value={
              localData.start_time_of_hospitalization
                ? new Date(
                    localData.start_time_of_hospitalization
                  ).toLocaleTimeString("ru-ru")
                : "00:00:00"
            }
            onChange={(e) =>
              handleChange("start_time_of_hospitalization", e.target.value)
            }
          />
        </HStack>
        <HStack>
          <Text>Время прибытия в стационар:</Text>
          <Input
            value={
              localData.time_of_arrival_at_hospital
                ? new Date(
                    localData.time_of_arrival_at_hospital
                  ).toLocaleTimeString("ru-ru")
                : "00:00:00"
            }
            onChange={(e) =>
              handleChange("time_of_arrival_at_hospital", e.target.value)
            }
          />
        </HStack>
        <HStack>
          <Text>Окончание вызова:</Text>
          <Input
            value={new Date(localData.call_end_time || " ").toLocaleTimeString(
              "ru-ru"
            )}
            onChange={(e) => handleChange("call_end_time", e.target.value)}
          />
        </HStack>
      </GridItem>
    </Grid>
  );
};

export default TimeDataTab;
