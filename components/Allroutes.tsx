import { getAllPages } from "nextra/context"

export function AllRoutes() {
    // const context = useContext();
    console.log(getAllPages())
    console.log(JSON.stringify(getAllPages()))
    return <>hi</>
}