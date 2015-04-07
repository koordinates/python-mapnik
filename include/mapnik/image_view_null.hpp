/*****************************************************************************
 *
 * This file is part of Mapnik (c++ mapping toolkit)
 *
 * Copyright (C) 2014 Artem Pavlenko
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 *****************************************************************************/

#ifndef MAPNIK_IMAGE_VIEW_NULL_HPP
#define MAPNIK_IMAGE_VIEW_NULL_HPP

#include <mapnik/image.hpp>

//stl
#include <stdexcept>

namespace mapnik {

template <>
class MAPNIK_DECL image_view<image_null>
{
public:
    using pixel_type = image_null::pixel_type;
    static const image_dtype dtype = image_null::dtype;
    
    image_view() {}
    ~image_view() {};
    
    image_view(image_view<image_null> const& rhs) {}
    image_view<image_null> & operator=(image_view<image_null> const& rhs) { return *this; }
    bool operator==(image_view<image_null> const& rhs) const { return true; }
    bool operator<(image_view<image_null> const& rhs) const { return false; }

    unsigned x() const { return 0; }
    unsigned y() const { return 0; }
    unsigned width() const { return 0; }
    unsigned height() const { return 0; }
    const pixel_type operator() (std::size_t i, std::size_t j) const { throw std::runtime_error("Can not get from a null image view"); }
    unsigned getSize() const { return 0; }
    unsigned getRowSize() const { return 0; }
    const pixel_type* getRow(unsigned row) const { return nullptr; }
    const pixel_type* getRow(unsigned row, std::size_t x0) const { return nullptr; }
    bool get_premultiplied() const { return false; }
    double get_offset() const { return 0.0; }
    double get_scaling() const { return 1.0; }
    image_dtype get_dtype() const { return dtype; }
};

} // end ns

#endif // MAPNIK_IMAGE_VIEW_NULL_HPP