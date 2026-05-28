#include <mapnik/config.hpp>
#include <mapnik/view_transform.hpp>
#include <pybind11/pybind11.h>

namespace py = pybind11;

using mapnik::view_transform;

namespace {

mapnik::coord2d forward_point(view_transform const& t, mapnik::coord2d const& in)
{
    mapnik::coord2d out(in);
    t.forward(out);
    return out;
}

mapnik::coord2d backward_point(view_transform const& t, mapnik::coord2d const& in)
{
    mapnik::coord2d out(in);
    t.backward(out);
    return out;
}

mapnik::box2d<double> forward_envelope(view_transform const& t, mapnik::box2d<double> const& in)
{
    return t.forward(in);
}

mapnik::box2d<double> backward_envelope(view_transform const& t, mapnik::box2d<double> const& in)
{
    return t.backward(in);
}

}

void export_view_transform(py::module const& m)
{
    py::class_<view_transform>(m, "ViewTransform")
        .def(py::init<int, int, mapnik::box2d<double> const&>())
        .def("forward", &forward_point)
        .def("backward", &backward_point)
        .def("forward", &forward_envelope)
        .def("backward", &backward_envelope)
        .def("scale_x", &view_transform::scale_x)
        .def("scale_y", &view_transform::scale_y)
        ;
}
